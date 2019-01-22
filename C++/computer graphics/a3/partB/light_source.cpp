/***********************************************************
Starter code for Assignment 3

This code was originally written by Jack Wang for
CSC418, SPRING 2005

implements light_source.h

***********************************************************/

#include <cmath>
#include <math.h>
#include <iostream>
#include "light_source.h"
#include <stdlib.h>
using namespace std;
double max(double a, double b) {
	return a < b ? b : a;
}

double _offset = 0.0000001;
vector<Ray3D> PointLight::get_shadow_rays(Ray3D& ray) {

	vector<Ray3D> shadow_rays;

	Ray3D shadowRay;

	shadowRay.origin = ray.intersection.point - _offset*ray.dir;
	shadowRay.dir = get_position() - shadowRay.origin;
	shadowRay.dir.normalize();

	shadow_rays.push_back(shadowRay);

	return shadow_rays;
}


void LightSource::shade(Ray3D& ray, double contribution) {
	// TODO: implement this function to fill in values for ray.col 
	// using phong shading.  Make sure your vectors are normalized, and
	// clamp colour values to 1.0.
	//
	// It is assumed at this point that the intersection information in ray 
	// is available.  So be sure that traverseScene() is called on the ray 
	// before this function.  
	Vector3D normal = ray.intersection.normal;
	normal.normalize();

	Vector3D lightSource = get_position() - ray.intersection.point;
	lightSource.normalize();

	Vector3D lightReflect = (2 * lightSource.dot(normal)) * normal - lightSource;
	lightReflect.normalize();

	Vector3D view = -ray.dir;
	view.normalize();

	Colour lightAmb = (ray.intersection.mat->ambient) * get_ambient();
	Colour lightDiff = max(0, lightSource.dot(normal)) * ray.intersection.mat->diffuse * get_diffuse();
	Colour lightSpec = max(0, pow((view.dot(lightReflect)), (ray.intersection.mat->specular_exp)))* (ray.intersection.mat->specular) * get_specular();
	Colour total = lightAmb + lightDiff + lightSpec;
	ray.col = ray.col + contribution * total;
	ray.col.clamp();

}



vector<Ray3D> Extendedlight::get_shadow_rays(Ray3D& ray) {

	vector<Ray3D> shadow_rays;
	vector<int> r;
	vector<int> s;
	Vector3D x = get_p();
	Vector3D y = get_q();

	int N = 40;

	r.clear();
	s.clear();
	
	//uniform random numbers in the range of [0, 1)
	for (int i = 0; i < N; i++) {
		r.push_back(((double)rand() / (RAND_MAX)+1));
		s.push_back(((double)rand() / (RAND_MAX)+1));
	}
	
	//shuffle points in array s[]
	double shuffle;
	for (int i = N - 1; i >= 0; i--) {
		int j = rand() % (i + 1);
		shuffle = s.at(j);
		s.at(j) = s.at(i);
		s.at(i) = shuffle;
	}

	Point3D origin = ray.intersection.point - _offset * ray.dir;
	for (int i = 0; i < N; i++) {

		Ray3D shadowRay;
		shadowRay.origin = origin;
		shadowRay.dir = get_position() + r.at(i) * x + s.at(i) * y - shadowRay.origin;
		shadowRay.dir.normalize();

		shadow_rays.push_back(shadowRay);
	}
	return shadow_rays;
}
