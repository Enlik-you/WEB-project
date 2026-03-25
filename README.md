# HiTrade

HiTrade is a full-stack wholesale marketplace for Korean products in the CIS region.

## Description

The purpose of this project is to develop a modern B2B-style web platform where users can browse Korean wholesale products, authenticate securely, interact with product data through APIs, and manage ordering-related actions.

This project is built according to the course requirements for both front-end and back-end development:
- Angular for the client side
- Django + Django REST Framework for the server side

## Project Goal

HiTrade is designed for suppliers and buyers in the CIS market who want to sell and purchase Korean goods in bulk through a convenient online platform.

## Main Features

- Wholesale catalog of Korean products
- Product categories
- User registration and login
- JWT authentication
- Product browsing and ordering
- Supplier and buyer interaction
- API-based communication between front-end and back-end
- Navigation between multiple pages
- Form handling and validation
- Error handling for failed API requests

## Front-End Requirements Coverage

The Angular front-end is planned to include:

- Interfaces and services for working with back-end APIs
- At least 4 click events that trigger API requests
- At least 4 form controls using `[(ngModel)]`
- Basic CSS styling for components
- Routing module with at least 3 named routes
- `@for` for looping over data and `@if` for conditional rendering
- JWT authentication
- HTTP interceptor for attaching tokens
- Login page and logout functionality
- Angular service using `HttpClient`
- Graceful API error handling

## Back-End Requirements Coverage

The Django + DRF back-end is planned to include:

- At least 4 models
- At least 2 ForeignKey relationships
- At least 2 serializers using `serializers.Serializer`
- At least 2 serializers using `serializers.ModelSerializer`
- At least 2 Function-Based Views (FBV)
- At least 2 Class-Based Views (CBV) using `APIView`
- REST API endpoints for front-end integration

## Planned Models

Possible models for the project:

- User
- Supplier
- Category
- Product
- Order
- OrderItem

## Tech Stack

### Front-End
- Angular
- TypeScript
- HTML
- CSS

### Back-End
- Django
- Django REST Framework
- Python

### Tools
- Git
- GitHub
- Postman

## Team Members

- Atimbekova Yenlik
- Symbat Mukhamedkarim
- Inkar Bakhytkali

## Project Status

Currently in development. Repository initialized, README added, and Angular project template created for the pre-defense stage.

## Purpose

This project is created for educational purposes as part of a university full-stack development assignment.