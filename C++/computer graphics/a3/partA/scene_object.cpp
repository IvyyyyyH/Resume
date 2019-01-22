/***********************************************************
Starter code for Assignment 3

This code was originally written by Jack Wang for
CSC418, SPRING 2005

implements scene_object.h

***********************************************************/

#include <cmath>
#include <iostream>
#include "scene_object.h"

bool UnitSquare::intersect(Ray3D& ray, const Matrix4x4& worldToModel,
	const Matrix4x4& modelToWorld) {
	// TODO: implement intersection code for UnitSquare, which is
	// defined on the xy-plane, with vertices (0.5, 0.5, 0), 
	// (-0.5, 0.5, 0), (-0.5, -0.5, 0), (0.5, -0.5, 0), and normal
	// (0, 0, 1).
	//
	// Your goal here is to fill ray.intersection with correct values
	// should an intersection occur.  This includes intersection.point, 
	// intersection.normal, intersection.none, intersection.t_value.   
	//
	// HINT: Remember to first transform the ray into object space  
	// to simplify the intersection test.

	Ray3D modelSpace = Ray3D(worldToModel*ray.origin, worldToModel*ray.dir);
	double t_value = -(modelSpace.origin[2] / modelSpace.dir[2]);
	Point3D x_check = modelSpace.origin + t_value*modelSpace.dir;

	if (t_value > 0) {
		if (x_check[0] >= -0.5&& x_check[0] <= 0.5 && x_check[1] >= -0.5&& x_check[1] <= 0.5) {
			if (ray.intersection.none || t_value < ray.intersection.t_value) {
				Intersection newIntersection;
				newIntersection.t_value = t_value;
				newIntersection.point = modelToWorld*x_check;
				newIntersection.none = false;
				newIntersection.normal = worldToModel.transpose()*Vector3D(0, 0, 1);
				ray.intersection = newIntersection;
				ray.intersection.normal.normalize();
				return true;
			}
		}
	}
	return false;
}



	
bool UnitSphere::intersect(Ray3D& ray, const Matrix4x4& worldToModel,
	const Matrix4x4& modelToWorld) {
	// TODO: implement intersection code for UnitSphere, which is centred 
	// on the origin.  
	//
	// Your goal here is to fill ray.intersection with correct values
	// should an intersection occur.  This includes intersection.point, 
	// intersection.normal, intersection.none, intersection.t_value.   
	//
	// HINT: Remember to first transform the ray into object space  
	// to simplify the intersection test.

	Ray3D modelSpace = Ray3D(worldToModel*ray.origin, worldToModel*ray.dir);
	Vector3D modelVector = modelSpace.origin - Point3D(0, 0, 0);
	double x = modelSpace.dir.dot(modelSpace.dir);
	double y = 2 * modelSpace.dir.dot(modelVector);
	double z = modelVector.dot(modelVector) - 1;
	double temp = y*y - 4 * x*z;
	double t_value;
	if (temp >= 0) {
		double root1 = (-y + sqrt(temp)) / (2 * x);
		double root2 = (-y - sqrt(temp)) / (2 * x);
		if (root1 > 0 || root2 > 0) {
			if (root1 > 0) {
				if (root2 > 0) {
					if (root1 >= root2) {
						t_value = root2;
					}
					else {
						t_value = root1;
					}
				}
				else {
					t_value = root1;
				}
			}
			else if (root2 > 0) {
				t_value = root2;
			}
			if (ray.intersection.none || (t_value > 0 && t_value < ray.intersection.t_value)) {
				Intersection newIntersection;
				Point3D newIntersectionModelSpace = modelSpace.origin + t_value*modelSpace.dir;
				newIntersection.point = modelToWorld*newIntersectionModelSpace;
				newIntersection.normal = worldToModel.transpose()*Vector3D(newIntersectionModelSpace[0], newIntersectionModelSpace[1], newIntersectionModelSpace[2]);
				newIntersection.t_value = t_value;
				newIntersection.none = false;
				ray.intersection = newIntersection;
				ray.intersection.normal.normalize();
				return true;
			}
		}


	}
	return false;
}

