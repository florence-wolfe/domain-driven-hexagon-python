# Domain Driven Hexagon Python Example

Here's an example repository to showcase how A domain driven architecture can be built with Python, Django, and Django Rest Framework.

There are certain challenges that needed to be overcome due to the technologies and the language used.

## Dependencies

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [injector](https://injector.readthedocs.io/en/latest/)
- [poetry](https://python-poetry.org/)

## Usage

```sh
poetry install
python -m ./manage.py runserver [PORT]
```

There 2 demo endpoints available:

1. [Find An Embedded Report](./rippling/reports_module/modules/embedded_report/application/queries/find_embedded_report/find_embedded_report_controller.py)
- GET `/reports/embedded_report`

Example Query Params:

```sh
?id=hello&title=hi&status=draft
```
2. [Create a Connected Report](./rippling/reports_module/modules/connected_report/application/commands/create_connected_report/create_connected_report_controller.py)
- POST `/reports/connected_report`

example body:

```json
{
  "id": "hi",
  "title": "new",
  "status": "draft"
}
```
### Code Structure

See this [domain-driven-hexagon repository](https://github.com/Sairyss/domain-driven-hexagon/) for an amazing writeup and a huge inspiration for this repository

The code directories are structured as follows:

- the primary entrypoint for the entire codebase is `reports_module`. This is the team's domain and is assumed to contain all of the application and configuration code needed.
Anything outside of that scope is assumed to belong to the parent application/project. For example, the `rippling/common` directory includes some common code that is reused across the application and among multiple teams.

- Inside the Reports Module you'll find the following:

  - `core` - contains reusable classes and functionality that can be used across the application. Not to be confused with a `utils` module that contains an assortment of unhoused functions, this folder would contain code such as our application configuration, constants, and the base classes for our domain.
  - `infrastructure` - contains the infrastructure code. What we mean by this is any code that needs to encapsulate specific technologies. This allows us to isolae message brokers, caches, databases, 3rd party services, ORM Entities, etc.
  - `modules` - contains the application code dividing by subdomain (as it's assumed that the aggregate domain is largely considered to be Reports)
  - the dependency injection container [reports_di_container.py](./rippling/reports_module/reports_di_container.py)
    - This container is setup to only need to be modified when a _new subdomain_ is being added.

Inside each module directory you'll find:

- `[module_name]_di_container.py` - contains the dependency injection container for that module
- `/application` - This folder is where the application code lives. In other words, the services, and controllers. They're split by commands and queries following CQRS
c  - You'll see subdirectories that are named based on use-case rather than by data or file type. For example, `application/commands/create_connected_report` contains the controller, and service for creating a connected report.
   - at the root of `/application` you'll find a domain service that is responsible for aggregate behaviors such as handling interactions with an external domain. An example of this can be found in the [EmbeddedReportService](./ripplijng/reports_module/modules/embedded_report/application/embedded_report_service.py)
- `/domain` - contains the domain code for that module. In other words, this is the schema and domain model that we expect our application to adhere to. This is our team's understanding of how that domain's data structure should be represented and managed.
- `/infrastructure` - contains the infrastructure code _specific to this module_. This is again code intended to be isolating technologies. In this case it should include repositories, data models, etc.
- `/interfaces` - contains the interfaces for the module.
  - An intentional decision was to avoid hiding the implementations of the code behind an `/spi` or other forms of abstractions. When following the architectural design principles dogmatically you can end up with an unwieldly folder structure that forces developers to be intimately familiar with _both_ the directory structure and the architectural concepts they apply.
  - See [hexagonal-architecture-django](https://github.com/BasicWolf/hexagonal-architecture-django/tree/main/src/myapp) for an example


## Decisions

- All domains are split up by commands and queries as per CQRS. This allows us to have use-case driven controllers and services and encourages developers to think more about behavior and business requirements rather than about data structures. This often facilitates feature development and code flexibility over time. Furthermore, this will allow services and controllers to be incredibly small.
  - This means that we go from `Request` (example: JSON, XML, etc.) -> `RequestDTO` (data transfer object. basically, some pythonic useable code) -> `Command` (describes _intent_ and the action that needs to be performed) -> `Service` -> `DB` -> `Service` ->`ResponseDTO` (the response format that we serialize to send back to the user)
- A top-level application service is created to allow cross boundary communication. This is unconventional but allows for the occasional times when boundaries cannot be completely isolated and depend on each other.
- The `core` directory is intentionally created to avoid the need to introduce abstractions that tend to drive confusion. Instead of multiple directories split by _layer_ we can store all of our core logic and omit the notion of adapters, ports,and other aspects of the code. Instead, the codebase applies these concepts without explicitly naming things as such, reducing the cognitive load.
- [Dependency Injection](https://en.wikipedia.org/wiki/Dependency_injection) is used to encourage loosely coupled modules as per [SOLID](https://en.wikipedia.org/wiki/Dependency_inversion_principle)
  - **The dependency injection providers should be the only sections of code that are aware of implementations**.
- Colocation is heavily encouraged. [Great co-location writeup](https://mtsknn.fi/blog/locality-of-behavior-and-co-location/#:~:text=The%20Co%2Dlocation%20principle%20states,where%20it's%20relevant%20as%20possible.)

## What's Left? What Can Be Improved?

- We can improve the type signature for the Request data to ensure that it adheres to the request DTO correctly. For example, you may notice a type error in the `CreateConnectedReportController` related to the str type not matching the enum's type.
- We can possibly move the `common` module which was intended to contain shared module behavior to the `core` folder, as this seems to serve a better intent.
- It would be great to create lint rules that would enforce some import boundaries — For example, it would be great to prevent _any_ file other than services to import implementation code.

Everything is subject to change. All of this is just based on my opinion.