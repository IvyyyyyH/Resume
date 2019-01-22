/***********************************************************
     Starter code for Assignment 3

     This code was originally written by Jack Wang for
		    CSC418, SPRING 2005

		Implementations of functions in raytracer.h, 
		and the main function which specifies the 
		scene to be rendered.	

***********************************************************/


#include "raytracer.h"
#include "bmp_io.h"
#include <cmath>
#include <iostream>
#include <cstdlib>

Raytracer::Raytracer() : _lightSource(NULL) {
	_root = new SceneDagNode();
}

Raytracer::~Raytracer() {
	delete _root;
}

SceneDagNode* Raytracer::addObject( SceneDagNode* parent, 
		SceneObject* obj, Material* mat ) {
	SceneDagNode* node = new SceneDagNode( obj, mat );
	node->parent = parent;
	node->next = NULL;
	node->child = NULL;
	
	// Add the object to the parent's child list, this means
	// whatever transformation applied to the parent will also
	// be applied to the child.
	if (parent->child == NULL) {
		parent->child = node;
	}
	else {
		parent = parent->child;
		while (parent->next != NULL) {
			parent = parent->next;
		}
		parent->next = node;
	}
	
	return node;;
}

LightListNode* Raytracer::addLightSource( LightSource* light ) {
	LightListNode* tmp = _lightSource;
	_lightSource = new LightListNode( light, tmp );
	return _lightSource;
}

void Raytracer::rotate( SceneDagNode* node, char axis, double angle ) {
	Matrix4x4 rotation;
	double toRadian = 2*M_PI/360.0;
	int i;
	
	for (i = 0; i < 2; i++) {
		switch(axis) {
			case 'x':
				rotation[0][0] = 1;
				rotation[1][1] = cos(angle*toRadian);
				rotation[1][2] = -sin(angle*toRadian);
				rotation[2][1] = sin(angle*toRadian);
				rotation[2][2] = cos(angle*toRadian);
				rotation[3][3] = 1;
			break;
			case 'y':
				rotation[0][0] = cos(angle*toRadian);
				rotation[0][2] = sin(angle*toRadian);
				rotation[1][1] = 1;
				rotation[2][0] = -sin(angle*toRadian);
				rotation[2][2] = cos(angle*toRadian);
				rotation[3][3] = 1;
			break;
			case 'z':
				rotation[0][0] = cos(angle*toRadian);
				rotation[0][1] = -sin(angle*toRadian);
				rotation[1][0] = sin(angle*toRadian);
				rotation[1][1] = cos(angle*toRadian);
				rotation[2][2] = 1;
				rotation[3][3] = 1;
			break;
		}
		if (i == 0) {
		    node->trans = node->trans*rotation; 	
			angle = -angle;
		} 
		else {
			node->invtrans = rotation*node->invtrans; 
		}	
	}
}

void Raytracer::translate( SceneDagNode* node, Vector3D trans ) {
	Matrix4x4 translation;
	
	translation[0][3] = trans[0];
	translation[1][3] = trans[1];
	translation[2][3] = trans[2];
	node->trans = node->trans*translation; 	
	translation[0][3] = -trans[0];
	translation[1][3] = -trans[1];
	translation[2][3] = -trans[2];
	node->invtrans = translation*node->invtrans; 
}

void Raytracer::scale( SceneDagNode* node, Point3D origin, double factor[3] ) {
	Matrix4x4 scale;
	
	scale[0][0] = factor[0];
	scale[0][3] = origin[0] - factor[0] * origin[0];
	scale[1][1] = factor[1];
	scale[1][3] = origin[1] - factor[1] * origin[1];
	scale[2][2] = factor[2];
	scale[2][3] = origin[2] - factor[2] * origin[2];
	node->trans = node->trans*scale; 	
	scale[0][0] = 1/factor[0];
	scale[0][3] = origin[0] - 1/factor[0] * origin[0];
	scale[1][1] = 1/factor[1];
	scale[1][3] = origin[1] - 1/factor[1] * origin[1];
	scale[2][2] = 1/factor[2];
	scale[2][3] = origin[2] - 1/factor[2] * origin[2];
	node->invtrans = scale*node->invtrans; 
}

Matrix4x4 Raytracer::initInvViewMatrix( Point3D eye, Vector3D view, 
		Vector3D up ) {
	Matrix4x4 mat; 
	Vector3D w;
	view.normalize();
	up = up - up.dot(view)*view;
	up.normalize();
	w = view.cross(up);

	mat[0][0] = w[0];
	mat[1][0] = w[1];
	mat[2][0] = w[2];
	mat[0][1] = up[0];
	mat[1][1] = up[1];
	mat[2][1] = up[2];
	mat[0][2] = -view[0];
	mat[1][2] = -view[1];
	mat[2][2] = -view[2];
	mat[0][3] = eye[0];
	mat[1][3] = eye[1];
	mat[2][3] = eye[2];

	return mat; 
}


void Raytracer::computeTransforms( SceneDagNode* node )
{
    SceneDagNode *childPtr;
    if (node->parent != NULL )
    {
        node->modelToWorld = node->parent->modelToWorld*node->trans;
        node->worldToModel = node->invtrans*node->parent->worldToModel; 
    }
    else
    {
        node->modelToWorld = node->trans;
        node->worldToModel = node->invtrans; 
    }
    // Traverse the children.
    childPtr = node->child;
    while (childPtr != NULL) {
        computeTransforms(childPtr);
        childPtr = childPtr->next;
    }



}

void Raytracer::traverseScene( SceneDagNode* node, Ray3D& ray ) {
    SceneDagNode *childPtr;

    // Applies transformation of the current node to the global
    // transformation matrices.
    if (node->obj) {
        // Perform intersection.
        if (node->obj->intersect(ray, node->worldToModel, node->modelToWorld)) {
            ray.intersection.mat = node->mat;
        }
    }
    // Traverse the children.
    childPtr = node->child;
    while (childPtr != NULL) {
        traverseScene(childPtr, ray);
        childPtr = childPtr->next;
    }

}

void Raytracer::computeShading( Ray3D& ray ) {
	LightListNode* curLight = _lightSource;
	vector<Ray3D> shadow_rays;
	Ray3D shadowRay;
	for (;;) {
		if (curLight == NULL) break;
		// Each lightSource provides its own shading function.

		// Implement shadows here if needed.

		shadow_rays = curLight->light->get_shadow_rays(ray);
		int numRay = shadow_rays.size();

		for (int i = 0; i < numRay; i++) {
			shadowRay = shadow_rays.at(i);
			// Check intesection
			traverseScene(_root, shadowRay);
			// Don't bother shading if the ray didn't hit 
			// anything.
			if (shadowRay.intersection.none) {
				curLight->light->shade(ray, 1.0 / numRay);
			}
			else {
				if (_shadows) {
					Colour ka = ray.intersection.mat->ambient;
					Colour Ia = curLight->light->get_ambient() * ka;
					ray.col = ray.col + (1.0 / numRay) * Ia * ka;
					ray.col.clamp();
				}
				else {
					curLight->light->shade(ray, 1.0 / numRay);
				}
			}
		}
		curLight = curLight->next;
	}
}

void Raytracer::initPixelBuffer() {
    int numbytes = _scrWidth * _scrHeight * sizeof(unsigned char);
    _rbuffer = new unsigned char[numbytes];
    std::fill_n(_rbuffer, numbytes,0);
    _gbuffer = new unsigned char[numbytes];
    std::fill_n(_gbuffer, numbytes,0);
    _bbuffer = new unsigned char[numbytes];
    std::fill_n(_bbuffer, numbytes,0);
}

void Raytracer::flushPixelBuffer( std::string file_name ) {
    bmp_write( file_name.c_str(), _scrWidth, _scrHeight, _rbuffer, _gbuffer, _bbuffer );
    delete _rbuffer;
    delete _gbuffer;
    delete _bbuffer;
}

Vector3D reflect(const Vector3D& I, const Vector3D& N) {
	return I - 2 * I.dot(N) * N;
}

Ray3D glossyReflect(Ray3D& ray, double blurDegree) {
	double x1 = (double)rand() / (RAND_MAX + 1);
	double x2 = (double)rand() / (RAND_MAX + 1);
	double u = -blurDegree / 2 + x1*blurDegree;
	double v = -blurDegree / 2 + x2*blurDegree;

	Vector3D R = ray.dir - 2 * ray.intersection.normal.dot(ray.dir)*ray.intersection.normal;
	R.normalize();

	Vector3D newDir = R + u*Vector3D(1, 0, 0) + v*Vector3D(0, 1, 0);
	Point3D newOrigin = ray.intersection.point - 0.000001*ray.dir;
	newDir.normalize();
	return Ray3D(newOrigin, newDir);
}


Colour Raytracer::shadeRay( Ray3D& ray ) {
	Colour colCurrentRay(0.0, 0.0, 0.0);
	Colour colReflection(0.0, 0.0, 0.0);
	Colour colRefraction(0.0, 0.0, 0.0);
    traverseScene(_root, ray); 

    // Don't bother shading if the ray didn't hit 
    // anything.
    if (!ray.intersection.none ) {
		computeShading(ray);
		colCurrentRay = ray.col;

		
		//reflection
		if (ray.maxDepth < _maxdepth) {

			//reflection
			Ray3D rayReflection = glossyReflect(ray, _bulrDegree);
			if (ray.intersection.normal.dot(rayReflection.dir) > 0) {
				rayReflection.maxDepth = ray.maxDepth + 1;
				colReflection = pow(ray.intersection.mat->reflection_coef, ray.maxDepth)*shadeRay(rayReflection);
			}
			else {
				colReflection = Colour(0, 0, 0);
			}
			//refraction
			double outside;
			double inside;

			// check the refaction ray is inside or outside
			// in order to define refraction index 
			if (ray.refraction_depth % 2 == 0) {
				outside = 1;
				inside = ray.intersection.mat->refrative_index;

			}
			else {
				outside = ray.intersection.mat->refrative_index;
				inside = 1;
			}

			double n = outside / inside;
			Vector3D direction = -ray.dir;
			direction.normalize();
			double temp = pow(ray.intersection.normal.dot(direction), 2);
			double d = 1.0 - n * n * (1.0 - temp);

			Vector3D dirRefraction;

			// Refraction ray
			Point3D originRefraction;
			if (d >= 0) {
				dirRefraction = (n * ray.intersection.normal.dot(direction) - sqrt(d)) * ray.intersection.normal - n * direction;
				originRefraction = ray.intersection.point + 0.0001 * ray.dir;
				dirRefraction.normalize();
				Ray3D refrRay(originRefraction, dirRefraction);
				refrRay.maxDepth = ray.maxDepth + 1;
				refrRay.refraction_depth = ray.refraction_depth + 1;
				colRefraction = pow(ray.intersection.mat->refrative_index, ray.maxDepth) * shadeRay(refrRay);
			}
			else {
				colRefraction = Colour(0, 0, 0);
			}
		}
    }

    // You'll want to call shadeRay recursively (with a different ray, 
    // of course) here to implement reflection/refraction effects.  
	colCurrentRay = colCurrentRay+ colRefraction + colReflection;
	colCurrentRay.clamp();
    return colCurrentRay; 
}	

void Raytracer::render( int width, int height, Point3D eye, Vector3D view, 
        Vector3D up, double fov, std::string fileName ) {
    computeTransforms(_root);
    Matrix4x4 viewToWorld;
    _scrWidth = width;
    _scrHeight = height;
	_shadows = true;
	_maxdepth = 3;
	_refraction_depth = 3;
	_antiAlis = 2;
    double factor = (double(height)/2)/tan(fov*M_PI/360.0);

    initPixelBuffer();
    viewToWorld = initInvViewMatrix(eye, view, up);

    // Construct a ray for each pixel.
    for (int i = 0; i < _scrHeight; i++) {
        for (int j = 0; j < _scrWidth; j++) {
            // Sets up ray origin and direction in view space, 
            // image plane is at z = -1.
            Point3D origin(0, 0, 0);
			Point3D imagePlane;
			imagePlane[2] = -1;
			Colour col;
			for (int a = 0; a < _antiAlis; a++) {
				for (int b = 0; b < _antiAlis; b++) {
					imagePlane[0] = (-double(width) / 2 + 0.5 + a * 0.25 + j) / factor;
					imagePlane[1] = (-double(height) / 2 + 0.5 + b * 0.25 + i) / factor;
					Ray3D ray;

					ray.maxDepth = 0;
					ray.refraction_depth = 0;
					ray.origin = viewToWorld*origin;
					ray.dir = viewToWorld*imagePlane - ray.origin;
					ray.dir.normalize();

					col = col + shadeRay(ray);
				}
			}

			// TODO: Convert ray to world space and call 
			// shadeRay(ray) to generate pixel colour. 	
			
			

			_rbuffer[i*width+j] = int(col[0]*255 / pow(_antiAlis, 2));
			_gbuffer[i*width+j] = int(col[1]*255 / pow(_antiAlis, 2));
			_bbuffer[i*width+j] = int(col[2]*255 / pow(_antiAlis, 2));
		}
	}

	flushPixelBuffer(fileName);
}

