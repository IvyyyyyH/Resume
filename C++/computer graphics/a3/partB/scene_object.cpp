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


bool UnitCylinder::intersect(Ray3D& ray, const Matrix4x4& worldToModel,
	const Matrix4x4& modelToWorld) {
	// convert ray to model space
	Ray3D modelSpace = Ray3D(worldToModel * ray.origin, worldToModel * ray.dir);
	// center of unit cyclinder
	Point3D center(0, 0, 0);
	double t_value = 0.;
	double temp1, temp2, temp;
	Vector3D normal;

	Point3D newIntersection;

	if (modelSpace.dir[2] == 0) {
		double x = pow(modelSpace.dir[0], 2) + pow(modelSpace.dir[1], 2);
		double y = 2 * (modelSpace.dir[0] * modelSpace.origin[0] +
			modelSpace.dir[1] * modelSpace.origin[1]);
		double z = pow(modelSpace.origin[0], 2) + pow(modelSpace.origin[1], 2) - 1;
		temp = y * y - 4 * x * z;

		if (temp > 0) {
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
				newIntersection = modelSpace.origin + t_value * modelSpace.dir;
				normal = Vector3D(newIntersection[0], newIntersection[1], 0);
				normal.normalize();
				if (newIntersection[2] < 0.5 && newIntersection[2] > -0.5) {

					if (ray.intersection.none || t_value < ray.intersection.t_value) {
						ray.intersection.point = modelToWorld * newIntersection;
						Point3D normalTemp;
						normalTemp[0] = newIntersection[0];
						normalTemp[1] = newIntersection[1];
						normalTemp[2] = 0;
						ray.intersection.normal = modelToWorld * (normalTemp - center);
						ray.intersection.t_value = t_value;
						ray.intersection.none = false;
						return true;
					}
				}
			}
		}
	}
	else {

		temp1 = (-0.5 - modelSpace.origin[2]) / modelSpace.dir[2];
		temp2 = (0.5 - modelSpace.origin[2]) / modelSpace.dir[2];

		if (temp1 < temp2) {
			t_value = temp1;
			normal = Point3D(0, 0, -1) - center;
		}
		else {
			t_value = temp2;
			normal = Point3D(0, 0, 1) - center;
		}
		normal.normalize();

		if (t_value > 0) {
			newIntersection = modelSpace.origin + t_value * modelSpace.dir;

			// face
			if (pow(newIntersection[0], 2) + pow(newIntersection[1], 2) <= 1) {
				if (ray.intersection.none || t_value < ray.intersection.t_value) {
					ray.intersection.point = newIntersection;
					ray.intersection.normal = normal;
					ray.intersection.t_value = t_value;
					ray.intersection.none = false;
					return true;
				}
			}

			// body

			double x = pow(modelSpace.dir[0], 2) + pow(modelSpace.dir[1], 2);
			double y = 2 * (modelSpace.dir[0] * modelSpace.origin[0] +
				modelSpace.dir[1] * modelSpace.origin[1]);
			double z = pow(modelSpace.origin[0], 2) + pow(modelSpace.origin[1], 2) - 1;
			temp = y * y - 4 * x * z;
			if (temp > 0) {
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
					newIntersection = modelSpace.origin + t_value * modelSpace.dir;
					normal = Vector3D(newIntersection[0], newIntersection[1], 0);
					normal.normalize();
					if (newIntersection[2] < 0.5 && newIntersection[2] > -0.5) {
						if (ray.intersection.none || t_value < ray.intersection.t_value) {
							ray.intersection.point = modelToWorld * newIntersection;
							ray.intersection.normal = modelToWorld * (Point3D(newIntersection[0], newIntersection[1], 0) - center);
							ray.intersection.t_value = t_value;
							ray.intersection.none = false;
							return true;
						}
					}

				}
			}
		}
	}
	return false;
}
