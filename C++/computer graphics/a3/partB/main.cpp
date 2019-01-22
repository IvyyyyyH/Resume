/***********************************************************
Starter code for Assignment 3

This code was originally written by Jack Wang for
CSC418, SPRING 2005

***********************************************************/


#include "raytracer.h"
#include <cstdlib>
#include <string> 

int main(int argc, char* argv[])
{
	// Build your scene and setup your camera here, by calling 
	// functions from Raytracer.  The code here sets up an example
	// scene and renders it from two different view points, DO NOT
	// change this if you're just implementing part one of the 
	// assignment.  
	Raytracer raytracer;
	int width = 360 * 2;
	int height = 240 * 2;

	if (argc == 3) {
		width = atoi(argv[1]);
		height = atoi(argv[2]);
	}

	// Camera parameters.
	Point3D eye(0, 0, 1);
	Vector3D view(0, 0, -1);
	Vector3D up(0, 1, 0);
	double fov = 60;

	// Defines a material for shading.
	// Defines a material for shading.
	Material gold(Colour(0.3, 0.3, 0.3), Colour(0.75164, 0.60648, 0.22648),
		Colour(0.628281, 0.555802, 0.366065),
		51.2, 0.0, 0.0);

	Material jade(Colour(0, 0, 0), Colour(0.54, 0.89, 0.63),
		Colour(0.316228, 0.316228, 0.316228),
		12.8, 0.34, 0.5);
	Material metal(Colour(0.1, 0.1, 0.1), Colour(0.6, 0.6, 0.6),
		Colour(0.7, 0.7, 0.3),
		51.2, 1.627, 0.8);

	Material glass(Colour(0.0, 0.0, 0.0), Colour(0.588235, 0.670588, 0.729412),
		Colour(0.9, 0.9, 0.9),
		96, 1.3, 0.8);
	
	/*	// Defines a point light source.
	raytracer.addLightSource(new PointLight(Point3D(0, 0, 5),
		Colour(0.9, 0.9, 0.9)));
	/*	point light*/
	
	raytracer.addLightSource(new Extendedlight(Point3D(0, 0, 5), Vector3D(2, 0, 0), Vector3D(0, 2, 0),
		Colour(0.9, 0.9, 0.9)));
	
	SceneDagNode*sphere = raytracer.addObject(new UnitSphere(), &gold);
	SceneDagNode*plane = raytracer.addObject(new UnitSquare(), &jade);
	SceneDagNode*cylinder = raytracer.addObject( new UnitCylinder(), &glass);

	// Apply some transformations to the unit square.
	double factor1[3] = { 1.0, 2.0, 1.0 };
	double factor2[3] = { 6.0, 6.0, 6.0 };
	raytracer.translate(sphere, Vector3D(-1., 0., -5.));

	raytracer.translate(plane, Vector3D(0., 0., -7.));
	raytracer.rotate(plane, 'z', 45);
	raytracer.scale(plane, Point3D(0., 0., 0.), factor2);

	raytracer.translate(cylinder, Vector3D(1., 1., -4.));
	raytracer.rotate(cylinder, 'x', 45);

	// Render the scene, feel free to make the image smaller for
	// testing purposes.	
	raytracer.render(width, height, eye, view, up, fov, "view1.bmp");

	// Render it from a different point of view.
	Point3D eye2(4., 2., 0.);
	Vector3D view2(-4., -2., -6.);
	raytracer.render(width, height, eye2, view2, up, fov, "view2.bmp");
	
	//the ball circles around an arbitrary point (-1, 0, -4), y = 0;
	double distance = 4;
	int max_num = 100;
	double t = 2 * M_PI / max_num;
	Point3D temp = Point3D(-1, 0., -5.);

	/*
	for (int i = 0; i < max_num; i++) {
		printf("%d\n", i);
		raytracer.translate(sphere, Point3D(-1 - cos(t*i), 0, -4 - sin(t*i)) - temp);
		temp = Point3D(-1 - cos(t*i), 0, -4 - sin(t*i));
		raytracer.render(width, height, eye2, view2, up, fov, "temp/"+to_string(i)+".bmp");
	}
	
	*/

	for (int i = 0; i < max_num; i++) {
		string filename = "temp/" + to_string(i) + ".bmp";
		bmp_print_test(filename.c_str());
		
	}
	
	return 0;
}

