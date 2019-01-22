#include <types.h>
#include <kern/errno.h>
#include <lib.h>
#include <machine/pcb.h>
#include <machine/spl.h>
#include <machine/trapframe.h>
#include <kern/callno.h>
#include <syscall.h>
#include <curthread.h>
#include <addrspace.h>
#include <thread.h>
#include <synch.h>
#include <vnode.h>
#include <uio.h>
#include "opt-synchprobs.h"
#include <kern/unistd.h>
#include <vfs.h>
#include <machine/spl.h>
#include <kern/limits.h>
#include <test.h>
#include <vm.h>


/*
 * System call handler.
 *
 * A pointer to the trapframe created during exception entry (in
 * exception.S) is passed in.
 *
 * The calling conventions for syscalls are as follows: Like ordinary
 * function calls, the first 4 32-bit arguments are passed in the 4
 * argument registers a0-a3. In addition, the system call number is
 * passed in the v0 register.
 *
 * On successful return, the return value is passed back in the v0
 * register, like an ordinary function call, and the a3 register is
 * also set to 0 to indicate success.
 *
 * On an error return, the error code is passed back in the v0
 * register, and the a3 register is set to 1 to indicate failure.
 * (Userlevel code takes care of storing the error code in errno and
 * returning the value -1 from the actual userlevel syscall function.
 * See src/lib/libc/syscalls.S and related files.)
 *
 * Upon syscall return the program counter stored in the trapframe
 * must be incremented by one instruction; otherwise the exception
 * return code will restart the "syscall" instruction and the system
 * call will repeat forever.
 *
 * Since none of the OS/161 system calls have more than 4 arguments,
 * there should be no need to fetch additional arguments from the
 * user-level stack.
 *
 * Watch out: if you make system calls that have 64-bit quantities as
 * arguments, they will get passed in pairs of registers, and not
 * necessarily in the way you expect. We recommend you don't do it.
 * (In fact, we recommend you don't use 64-bit quantities at all. See
 * arch/mips/include/types.h.)
 */

void
mips_syscall(struct trapframe *tf)
{
    int callno;
    int32_t retval;
    int err;
    int byte;
    assert(curspl==0);

    callno = tf->tf_v0;

    /*
     * Initialize retval to 0. Many of the system calls don't
     * really return a value, just 0 for success and -1 on
     * error. Since retval is the value returned on success,
     * initialize it to 0 by default; thus it's not necessary to
     * deal with it except for calls that return other values, 
     * like write.
     */

    retval = 0;

    switch (callno) {
      case SYS_reboot:
      err = sys_reboot(tf->tf_a0);
      break;
      case SYS_fork:
        err = sys_fork(tf, &retval);
      break;
      case SYS_waitpid:
        err = sys_waitpid(tf->tf_a0, tf->tf_a1, tf->tf_a2, &retval);
      break;
      case SYS__exit:
        sys__exit(tf->tf_a0);
        err = 0;
      break;
        case SYS_getpid:
        retval = sys_getpid();
        err = 0;
      break;
        case SYS_write:
        err = sys_write(tf->tf_a0, (void *) tf->tf_a1, (size_t)tf->tf_a2);
      break;
      case SYS_read:
        err = sys_read(tf->tf_a0, (void *) tf->tf_a1, (size_t)tf->tf_a2, &retval);
      break;
      case SYS_execv:
        retval = sys_execv((char *)tf->tf_a0,(char **)tf->tf_a1);
      err = 0;
      break;
        /* Add stuff here */
    
      case SYS_sbrk:
          retval = sys_sbrk((int)tf->tf_a0);
          err = 0;
        break;
    
      default:
      kprintf("Unknown syscall %d\n", callno);
      err = ENOSYS;
      break;
    }

    

    if (err) {
      /*
       * Return the error code. This gets converted at
       * userlevel to a return value of -1 and the error
       * code in errno.
       */
      tf->tf_v0 = err;
      tf->tf_a3 = 1;      /* signal an error */
    }
    else {
      /* Success. */
      tf->tf_v0 = retval;
      tf->tf_a3 = 0;      /* signal no error */
    }
    
    /*
     * Now, advance the program counter, to avoid restarting
     * the syscall over and over again.
     */
    
    tf->tf_epc += 4;

    /* Make sure the syscall code didn't forget to lower spl */
    assert(curspl==0);
}

int sys_read(int fd, char* buf, size_t size, int* retval) {
    char c;
    c = getch();
    if(c == '\r'){
      c = '\n';
    }
    *buf=c;
    size=sizeof(char);
    *retval = (int) c;
    return 0;
}


void md_forkentry(struct trapframe *tf, unsigned long as_data){
    /*
     * This function is provided as a reminder. You need to write
     * both it and the code that calls it.
     *
     * Thus, you can trash it and do things another way if you prefer.
     */

    struct trapframe tf_local;
    struct trapframe* childtf;
    //address space for the child thread
    struct addrspace* child_addr = (struct addrspace*) as_data;

    //put the new malloced trapframe on the child userstack
    tf_local = *tf;
    childtf = &tf_local;

    childtf->tf_v0 = 0;
    childtf->tf_a3 = 0;
    childtf->tf_epc += 4;

    curthread->t_vmspace = child_addr;

    as_activate(curthread->t_vmspace);

    mips_usermode(&tf_local);
}

int sys_fork(struct trapframe* tf, int* retval) {

    struct thread* newthread;
    struct trapframe* childtf;
    struct addrspace* child_addr;

    int result;
    if(curthread-> pid >= MAXPID){
        return EAGAIN;
    }
    childtf = (struct trapframe*) kmalloc(sizeof(struct trapframe));
    if (childtf == NULL) {
        kfree(childtf);
        return ENOMEM;
    }
    
    //copy the trapframe from parent to child in kernel level
    *childtf = *tf;

    //copy the data from parent address space into child thread
    int ret = as_copy(curthread->t_vmspace, &child_addr);
    if (child_addr == NULL) {
        kfree(childtf);
        return ENOMEM;
    }
    if (ret != 0){
        kfree(childtf);
        return ENOMEM;
    }

    as_activate(curthread->t_vmspace);

    result = thread_fork(curthread->t_name, childtf,(unsigned long)child_addr,(void (*)(void *, unsigned long)) md_forkentry,&newthread);

    if (result) {
        kfree(childtf);
        return ENOMEM;
    }
    

    *retval = (int) newthread->pid;

    return 0;
}

int sys__exit (int exitcode) {
    struct process* ptr = curthread->array_ptr;
    ptr->status = PROCESS_STOP;
    ptr->exitcode = exitcode;
    lock_acquire(process_lock);
    struct process* curr = curthread->array_ptr;
    cv_signal(curr->array_cv, process_lock);
    thread_exit();
    return 0;
}

int sys_getpid (void) {
    return (int)curthread->pid;
}


int sys_waitpid (pid_t pid, int* status, int options, int* retval) {
    if (options != 0){ 
        return EINVAL;
    }
    if (status == NULL){
        return EFAULT;
    }
    struct process* child = NULL;
    child = get_process(pid);
    if (child == NULL){ 
        return EFAULT;
    }

    lock_acquire(process_lock);
    
    if (child->ppid != curthread->pid) {
        lock_release(process_lock);
        return EINVAL;
    }
    if(child->ppid == curthread->pid){
        if(child->status == PROCESS_STOP){
             *status = child->exitcode;
             lock_release(process_lock);
        } else {
            cv_wait(child->array_cv,process_lock);
            *status = child->exitcode;
            lock_release(process_lock);
        }
    }
    lock_release(process_lock);
    *retval = (int) child->pid;
    return 0;
}



int sys_write(int filehandle, const void *buf, size_t size){
    if(filehandle < 0  || filehandle > 2){
        return EBADF;
    }
    if(buf == NULL){
        return EFAULT;
    }
    char* temp = (char*) buf;
    temp[size]='\0';
    kprintf("%s", temp);
    return 0;
}

int sys_execv(char *program, char **args)
{
    
    struct vnode *v;
    int result, argc, spl;
    int *length;
    size_t buflen;
    int i = 0;
    int j = 0;
    int k = 0;
    spl=splhigh();
    vaddr_t entrypoint, stackptr;
    char *progname = (char*)kmalloc(PATH_MAX); 
    copyinstr((userptr_t)program,progname,PATH_MAX,&buflen);
    char **argv= (char **)kmalloc(sizeof(char*));

      if(progname == NULL){
          return ENOMEM;
      }

      while (args[i]!=NULL){
          i++;
      }
      argc = i;

      if(argv == NULL){
          kfree(progname);
          return ENOMEM;
      }
      

      //In here we may need to free
      for (i=0; i<argc; i++){
          length[i] = strlen(args[i]);
          length[i]=length[i]+1;
      }
      for (i=0; i<=argc; i++){
          if(i<argc){  
              argv[i]=(char*)kmalloc(length[i]+1);
              if(argv[i]==NULL) {
                  return ENOMEM;
              }
                copyinstr((userptr_t)args[i], argv[i], length[i], &buflen);
          }
          else
          argv[i] = NULL;
    }


    int arglength[argc];
    int arg_pointer[argc];
    int offset=0;

    //passing the arglength of argv
    int count;
    for(count = argc-1; count >= 0; count--) {
        arglength[count] = strlen(argv[count])+1;
    }

    /* Open the file. */
    result = vfs_open(progname, O_RDONLY, &v);
    if (result) {
        return result;
    }


    if (curthread->t_vmspace) 
    {
        struct addrspace *as = curthread->t_vmspace;
        curthread->t_vmspace = NULL;
        as_destroy(as);
    }
    
    /* We should be a new thread. */
    assert(curthread->t_vmspace == NULL);

    /* Create a new address space. */
    curthread->t_vmspace = as_create();
    if (curthread->t_vmspace==NULL) {
        vfs_close(v);
        return ENOMEM;
    }

    /* Activate it. */
    as_activate(curthread->t_vmspace);


  /* Create a new address space. */
    curthread->t_vmspace = as_create();
    if (curthread->t_vmspace==NULL) {
        vfs_close(v);
        return ENOMEM;
    }

    /* Activate it. */
    as_activate(curthread->t_vmspace);

    /* Load the executable. */
    result = load_elf(v, &entrypoint);
    if (result) {
        /* thread_exit destroys curthread->t_vmspace */
        vfs_close(v);
        return result;
    }

    /* Done with the file now. */
    vfs_close(v);

    /* Define the user stack in the address space */
    result = as_define_stack(curthread->t_vmspace, &stackptr);
    if (result) {
        /* thread_exit destroys curthread->t_vmspace */
        return result;
    }

    
    
    for(i = argc-1; i >= 0; i--) {
        offset=(arglength[i] + (4-(arglength[i]%4)));
        stackptr = stackptr - offset;
        copyoutstr(argv[i], (userptr_t)stackptr, (size_t)arglength[i], &buflen);
        arg_pointer[i] = stackptr;
    }


    arg_pointer[argc] = (int)NULL;
    i = argc;
    while(i>=0){
        stackptr = stackptr - 4;
        copyout(&arg_pointer[i] ,(userptr_t)stackptr, sizeof(arg_pointer[i]));
        i--;
    }



    kfree(argv);
    kfree(progname);
    splx(spl);

    md_usermode(argc , (userptr_t)stackptr, stackptr, entrypoint);
    panic("md_usermode returned\n");
    return EINVAL;
}





struct process* get_process (pid_t pid) {
    if (pid > MAXPID || pid < MINPID) {
      //kprintf("error: pid out of range\n");
      return NULL;
    }
    int i;
    for(i = MINPID; i <= MAXPID; i++){
      if((pid_t)i == pid){
        if(array_table[i] == NULL){
          return NULL;
        }
        else{
          return array_table[i];
        }
      }
    }
    return NULL;
}



pid_t next_pid (void) {
    //check the process table is NULL or not
    if(array_table == NULL){
      return -1;
    }
   //find next null space in the array
    int i ;
    for (i = MINPID; i < MAXPID; i++){
        if(array_table[i] == NULL)
            return (pid_t)i;
    } 

    return -1; 
}



int sys_sbrk(int size) {
    int spl = splhigh();
    struct addrspace *as;
    as=curthread->t_vmspace;
    u_int32_t break_v, newheap;
    //size is invailded
    if (size >= malloc_limit) {
      splx(spl);
      return -1;
    }
    newheap= as->heap_end + (unsigned)size;
    break_v= as->heap_end;
    if ((newheap - as->heap_start)>heap_size) {
      splx(spl);
      return -1;
    }
    as->heap_end=newheap;
    splx(spl);
    return break_v;
}