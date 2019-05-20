# Harsh Realm Unit Designer

This application has the following objectives:

* Provide a decent template for creating flask apps
* Experiment with UI/UX and API features
* Experiment with back-ends like Redis, Mongo, etc.

### Google Doc Style

ref: http://google.github.io/styleguide/pyguide.html

Use hanging indents of 2 to 4 spaces for lines over 80 characters long

#### Modules

Docstring with file name and description

#### Functions

Enough documentation to write a call to the function without reading the code.

Args: List each parameter by name, then a description separated by a colon. If type annotations are not present, describe the type

Returns: Describe the type and semantics of the return value

Raises: List all exceptions that are relevant to the interface

#### Classes

Docstring below the class definition

Attributes: Document public attributes

#### Other Locations

Comment anything that would need to be explained in a code review

### Patterns for Relationships

#### 1-to-N
* Embedded documents
* List (Array) of Object IDs
* Parent Object ID