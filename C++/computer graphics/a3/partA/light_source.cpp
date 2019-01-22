/***********************************************************
     Starter code for Assignment 3

     This code was originally written by Jack Wang for
		    CSC418, SPRING 2005

		implements light_source.h

***********************************************************/

#include <cmath>
#include "light_source.h"

double max(double a, double b) {
	if (a > b)
		return a;
	return b;
}
void PointLight::shade( Ray3D& ray ) {
	// TODO: implement this function to fill in values for ray.col 
	// using phong shading.  Make sure your vectors are normalized, and
	// clamp colour values to 1.0.
	//
	// It is assumed at this point that the intersection information in ray 
	// is available.  So be sure that traverseScene() is called on the ray 
	// before this function.  
	


	Vector3D normal = ray.intersection.normal;
	normal.normalize();

	Vector3D lightSource = _pos - ray.intersection.point;
	lightSource.normalize();

	Vector3D lightReflect = 2*lightSource.dot(normal)*normal - lightSource;
	lightReflect.normalize();

	Vector3D view = -ray.dir;
	view.normalize();

	Colour lightAmb = (ray.intersection.mat->ambient)*_col_ambient;
	Colour lightDiff = max(0, lightSource.dot(normal))*(ray.intersection.mat->diffuse)*_col_diffuse;
	Colour lightSpec = pow(max(0, view.dot(lightReflect)), ray.intersection.mat->specular_exp)*(ray.intersection.mat->specular)*_col_specular;
	Colour total = ray.col + lightAmb + lightDiff + lightSpec;

	ray.col = total;
	ray.col.clamp();
	

}

/*Sig*/
/*
Intersection intersection = ray.intersection;
ray.col = intersection.mat->diffuse;
ray.col.clamp();
*/


/*only the diffuse and ambient*/

/*
Vector3D normal = ray.intersection.normal;
normal.normalize();

Vector3D lightSource = _pos - ray.intersection.point;
lightSource.normalize();

Vector3D lightReflect = (2 * lightSource.dot(normal))*normal - lightSource;
lightReflect.normalize();

Vector3D view = -ray.dir;
view.normalize();

Colour lightAmb = (ray.intersection.mat->ambient)*_col_ambient;
Colour lightDiff = max(0, lightSource.dot(normal))*(ray.intersection.mat->diffuse)*_col_diffuse;
Colour total = ray.col + lightAmb + lightDiff;

ray.col = total;
ray.col.clamp();
*/

/*phong*/
/*

Vector3D normal = ray.intersection.normal;
normal.normalize();

Vector3D lightSource = _pos - ray.intersection.point;
lightSource.normalize();

Vector3D lightReflect = (2 * lightSource.dot(normal))*normal - lightSource;
lightReflect.normalize();

Vector3D view = -ray.dir;
view.normalize();

Colour lightAmb = (ray.intersection.mat->ambient)*_col_ambient;
Colour lightDiff = max(0, lightSource.dot(normal))*(ray.intersection.mat->diffuse)*_col_diffuse;
Colour lightSpec = pow(max(0, view.dot(lightReflect)), ray.intersection.mat->specular_exp)*(ray.intersection.mat->specular)*_col_specular;
Colour total = ray.col + lightAmb + lightDiff  + lightSpec;

ray.col = total;
ray.col.clamp();
*/