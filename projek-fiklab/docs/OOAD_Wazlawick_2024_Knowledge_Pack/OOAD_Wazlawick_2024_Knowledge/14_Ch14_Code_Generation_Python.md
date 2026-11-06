<!-- Knowledge file: Chapter 14 — Code generation -->
> **About this file.** Chapter 14 of a cleaned, AI-ready edition of Wazlawick, R. S. (2024). Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-443-13739-6.  
> **Covers:** Code generation in Python: classes, attributes, basic get/set/add/remove methods by association type, collections, qualified associations, association classes, methods from dynamic models.  
> **Use this file when:** implementing a class diagram in code (Python examples).  
> **Sections:** 14.1 Introduction to code generation (p. 279); 14.2 Unidirectional associations (p. 286); 14.3 Bidirectional associations (p. 299); 14.4 Delegated methods and system operations (p. 305)  
> **Contains:** 19 figures transcribed as text, 26 code listings.

# Chapter 14: Code generation

*Source: Wazlawick, Object-Oriented Analysis and Design for Information Systems, 2nd ed. (Elsevier, 2024), starts p. 279*

## Key topics in this chapter (Chapter 14)

- Code generation for classes, attributes, and associations

- Code generation for delegated methods and system operations

- Patterns for bidirectional associations

## 14.1 Introduction to code generation

*Chapter 14 · p. 279*

In order to have running systems, it is necessary to generate code for the classes from the domain tier and for the other technological tiers of the system. This chapter concentrates on code generation for the domain tier.

Once the sequence diagrams and the DCD are produced, code generation is an activity that may be systematized to a point that it can be practically done automatically. Automatic code generation is feasible for domain classes, which perform all the logical processing specified by the system operation contracts.

This chapter presents rules for code generation for the DCD and sequence diagrams. Examples are presented in Python, which is nowadays a dominant language in learning and business. It also has structures that are much closer to those of the algorithms than other languages.

DCD classes are usually directly converted into programming language classes. Class attributes are converted into private instance variables in the respective class. In many languages, those variables must be declared. But this is not necessary in Python. As soon as a new identifier is used in the context of a class, it is assumed to be a new instance variable.

Although Python does not demand variables to be labeled, any variable has a type that is the type of the object that is stored in the variable. As explained before, variables that represent attributes must store alphanumeric values, such as Integer, Real, String, and Boolean, primitive ones, such as Date, Money, and ISBN, or enumerations such as CalendarDay, Gender, and PhoneType.

If other objects can access the attribute, then it is public and should be implemented with a getter method. If the attribute can be updated, then it must be implemented with a setter, which can be a simple set_attribute method or another variation such as increment_attribute, if the attribute is numeric. Fig. 14–1 presents an example of design classes that are used to show how programming code can be generated. 

281

**Figure 14–1: A reference class model for code generation.** *(p. 282)*

> **Diagram content (transcribed from the figure image):** Class diagram for code generation: Book {«imm» «unique» +isbn: ISBN; «imm» +title: String; +price: Money; «imm» +page_count: Natural; +/publisher_name: String = publisher.name; «opt» +cover_image: Image; +quantity_in_stock: Natural = 0}; Book * —«imm» author 1..*— Person {+id: PersonId; +name: String}; Book * —«imm» publisher 1— PublishingHouse {+name: String}.

**Figure 14–2: A design version for the conceptual model in Fig. 14–1.** *(p. 282)*

> **Diagram content (transcribed from the figure image):** Design class diagram with methods: Book private attributes (-isbn, -title, -price, -page_count, -cover_image, -quantity_in_stock = 0) and public methods +Book(an_isbn: ISBN, a_title: String, a_price: Money, a_page_count: Natural, a_set_of_authors: Set<Person>, a_publishing_house: PublishingHouse); +get_isbn(); +get_title(); +get_price(); +set_price(a_price); +get_page_count(); +get_publisher_name(); +get_cover_image(); +set_cover_image(cover_image); +get_quantity_in_stock(); +set_quantity_in_stock(a_quantity); +get_author(): Set<Person>; +get_publisher(): PublishingHouse. Person {-id: PersonId; -name: String; +Person(an_id, a_name); +get_id(); +get_name(); +set_name(a_name)}; PublishingHouse {-name; +PublishingHouse(a_name); +get_name()}.

First let us open a BIG parenthesis here to show the difference between a conceptual and a design class. What we see in Fig. 14–1 is a conceptual version of classes Book, Person, and PublishingHouse. Now compare it to Fig. 14–2 to see what a design or dominion definition for these classes could be:

Let us examine the differences and how the former diagram was transformed into this one. First, all attributes are transformed from public to private. And, if there is any derived attribute or association, it must be transformed into a public method.

In each of the classes, only the mandatory basic commands should be implemented. First, the Creator command, which in the case of Book has a lot of initialization parameters, including a set of Person and an instance of PublishingHouse.

All attributes that were public before now have a getter to access their values. All nonderived and nonimmutable ones will also have a setter that allows to change their values. In the case of roles from Book, in this diagram, both are immutable. Thus they implement only the getter methods and not the add, remove, and replace methods.

The derived attribute publisher_name from the conceptual model was found to be redundant here because the name of the publisher can be easily obtainable through the method get_publisher; thus, this derived attribute is wiped out of the model.

The two associations from Book are considered (for now) to be unidirectional, because during development, it was always the book that sends messages to the person or to the publishing house. Vice versa never happens. In this case, the associations are considered unidirectional until a case is found where a message must navigate to the opposite side. In this case, the association becomes bidirectional and must be implemented as that. At least a get_book method should be implemented in any class that may have access to the book.

Given all this features, we believe that for educational purposes, we should continue to work with the conceptual version of the classes, not the design one. Remember that the transformation from conceptual to design may be done at any moment between modeling and code implementation. Therefore in the following examples, we will take the conceptual classes as basis and generate code directly to python without making explicit the design version of each class.

Now, let us close those BIG parentheses and continue our analysis on the conceptual model.

Initially, we are going to program the class Book. First, declare the name of the class with the expression “class Book:.” In Python, upper and lower cases are considered different symbols. Thus if you write Class Book:, you will get an error because the expression Class is unknown to Python, but class is.

First thing usually is to define the initialization of the class. The constructor is a predefined command we do not need to worry by now. What we need to know is that the constructor, when activated to create a new instance of any class, will call a special method __init__ (two underlines before and after the word init. No spaces!). The parameters of __init__ should be, first, a special variable called “self ” followed by a list of parameters necessary to initialize the mandatory attributes and associations.

This list comprises attributes that are not optional neither derived. Unique attributes must be checked. But for now, we assume that this is going to be done later and proceed with them as if this stereotype is not present.

The first object that must appear as parameter of __init__ is self. Then, we can include the parameters the multiplicity of which does not accept 0, that is, the list would contain usually roles for which multiplicity is 1 or 1..– , or any other variation excluding 0.

In our example, the initial lines for creating the class Book in Python would be something like:

```python
class Book:
    def __init__(self, an_isbn, a_title, a_price,
                a_page_count, a_publishing_house, a_set_of_authors):
```

Next, we must assign to each attribute or association, which will be the instance variables, the values received by __init__. Later, we will discuss a more adequate approach to deal with associations, but for now we will just treat them as mere attributes. We just separate attributes and associations in two blocks marked by comments as seen below: 

```python
class Book:
    def __init__(self, an_isbn, a_title, a_price,
                a_page_count, a_publishing_house, a_set_of_authors):
    #ATTRIBUTES
        self.isbn = an_isbn
        self.title = a_title
        self.price = a_price
        self.page_count = a_page_count
        self.quantity_in_stock = 0
    #ASSOCIATIONS
        self.publishing_house = a_publishing_house
        self.authors = a_set_of_author
```

Now we will define the methods that are necessary for dealing with the attributes. Remember that:

- A normal attribute has methods set and get even if it is optional or have an initial value.

- Immutable attributes have only the get method, not the set.

- Derived attributes have only the get method that usually must be implemented as a more complex query than in the other cases.

In the case of associations:

- Normal associations have get, add, and removal methods unless other rules apply.

- Derived associations only have get.

- If the association is immutable, then it implements only the get method.

- Associations to 1 may have a get method. They also have a replace method if the business rules allow the object in that role to be replaced. They do not implement add and remove.

- Associations with a qualified role in the origin may implement get, add, and remove, normally, but they can also implement the method that finds an instance depending on its key: get_at(key). They can also have a second remove method: remove_at(key). The original one, applied on collections in general, receives the object to be removed as parameter (remove_role(object)). If it is a qualified association, though, it can also have a remove method based in the key (remove_role_at(key)). Also, if the qualifier is external, then the add method must explicitly indicate the key, such as add_role(key, value). In this case, the add method implemented to other collections with only the object to be added does not exist.

- In the case of an ordered role, get, add, and remove based on the object’s position may also be implemented additionally to their counterparts that use only the object as parameter. If this association has a replace method, then another replace method based on position may also be implemented.

The final code to implement the Book class with its basic methods would be like:

```python
class Book:
    def __init__(self, an_isbn, a_title, a_price, a_page_count,
                a_publishing_house, a_set_of_authors):
    #ATTRIBUTES
        self.isbn = an_isbn
        self.title = a_title
        self.price = a_price
        self.page_count = a_page_count
        self.quantity_in_stock = 0
    #ASSOCIATIONS
        self.publishing_house = a_publishing_house
        self.authors = a_set_of_authors
    #ATTRIBUTES
    def get_isbn(self):
        return self.isbn
    def get_title(self):
        return self.title
    def get_price(self):
        return self.price
    def set_price(self, new_price):
        self.price = new_price
    def get_page_count(self):
        return self.page_count
    def get_cover_image(self):
        return self.cover_image
    def set_cover_image(self, new_cover_image):
        self.cover_image = new_cover_image
    def get_quantity_in_stock(self):
        return self.quantity_in_stock
    def set_quantity_in_stock(self, new_quantity):
        self.quantity_in_stock = new_quantity
    #ASSOCIATIONS
    def get_publisher(self):
        return self.publishing_house
    def get_authors(self):
        return self.authors
```

**Table 14–1: Minimum set of basic methods to implement according to the kind of attribute role.**

```text
              (default)                 <<imm>>                   <<opt>>
get           get_role():alphanumeric   get_role():alphanumeric   get_role():alphanumeric
set           set(alphanumeric)         -x-                       set(alphanumeric)
Parameter     Yes                       Yes                       No
in __init__
                        Derived                     Initial value
get                       get_role():alphanumeric     get_role():alphanumeric
set                       -x-                         set(alphanumeric)
Parameter in __init__     No                          No
```

||**(default)**||**<<imm>>**|**<<opt>>**|
|---|---|---|---|---|
|**get**|get_role()|:alphanumeric|get_role():|alphanumeric get_role():alphanumeric|
|**set**|set(alphan|umeric)|-x-|set(alphanumeric)|
|**Parameter**|Yes||Yes|No|
|**in __init__**|||||
|||**Derived**||**Initial value**|
|**get**||get_role():al|phanumeric|get_role():alphanumeric|
|**set**||-x-||set(alphanumeric)|
|**Parameter in**|**__init__**|No||No|

Table 14–1 presents a summary of the basic methods that must be implemented for each kind of association role. Notice that some conditions can be combined. For example, a role may be to 0..1 and immutable at the same time. In this case, the strongest restriction applies. In the example, despite an association to 0..1 may implement add and remove methods, they will not be implemented because the stereotype «imm» does not allow it.

Observe that in Table 14–2, each kind of association has a different set of methods for accessing and changing links. The implementation of these methods follows definitions that are usually very similar from class to class. The following subsections show examples of some of those methods.

## 14.2 Unidirectional associations

*Chapter 14 · p. 286*

Unidirectional associations with no multiplicity constraints at the origin may be implemented similarly to attributes as instance variables, and according to Table 14–2, they should have methods for updating and querying.

However, if there are multiplicity constraints at the origin role, these associations must be considered as bidirectional, even if they are not navigable in both directions. Fig. 14–3 shows an example of that situation, where although the association is only navigable from Car to Person, every car must be linked to a single person.

If the association is implemented as an instance variable in the Person class, it will be hard to assure that a car belongs to a single person, which is a constraint in the origin.

There are still some considerations we must discuss about the differences between an attribute and a unidirectional association. First, attributes are always implemented by variables whose types are alphanumeric, primitive, or enumerations. Associations, on the other hand, are implemented by variables whose types are domain classes (in the case of associations to one) or data structures (in the case of associations to many).

In addition, considering different role multiplicities and other features of associations, there are distinctions to be made regarding the methods to be implemented for each type of association.

### 14.2.1 Unidirectional association to 1 and 0..1 — 14.2 Unidirectional associations

The unidirectional association with role multiplicity 1 may be stored in a single instance variable in the origin class, and its type should be the destination class. Fig. 14–4 shows a unidirectional association to one from Car to Person with role name owner.

**Table 14–2: Minimum set of basic methods to implement according to the kind of attribute role.**

```text
              to 1 (set)          to 0..1 (set)     to * (set)            to 1..* (set)
get           get_role():Object   get_role():Set    get_role():Set        get_role():Set
add           -x-                 add_role(object)  add_role(object)      add_role(object)
remove        -x-                 remove_role()     remove_role(object)   remove_role(object)
replace       replace(object)1      -x-               -x-                   -x-
Parameter     Yes                 No                No                    Yes
in __init__
                        <imm>               derived             with initial value
get                     get_role():Set      get_role():Set      get_role():Set
add                     -x-                 -x-                 add_role(object)
remove                  -x-                 -x-                 remove_role(object)
replace                 -x-                 -x-                 -x-
Parameter in __init__   Yes                 No                  No
          Bag                   OrderedSet                     Sequence
get       get_role():Bag        get_role():OrderedSet          get_role():Sequence
                                get_role(position):Object      get_role(position):Object
add       add_role(object)      add_role(position,object)      add_role(position,object)
remove    remove_role(object)   remove_role(object)            remove_role(position,object)
                                remove_role(position,object)
replace   -x-                   replace_role(position,object)  replace_role(position,object)
          Map (internal qualifier)  Map (external qualifier)
get       get_role():Set            get_role():Set
          get_role(key):Object      get_role(key):Object
add       add_role(object)          add_role(key,object)
remove    remove_role(object)       remove_role(object)
          remove_role(key)          remove_role(key)
replace   -x-                       replace_role(key,object)
          Partition (internal qualifier)   Partition (external qualifier)
get       get_role():Set                   get_role():Set
          get_role(key):Set                get_role(key):Set
add       add_role(object)                 add_role(key,object)
remove    remove_role(object)              -x-
replace   -x-                              -x-
          Set with association class            Array
get       get_role():Set                        get_role():Sequence
          get_association_role():Set            get_role(position):Object
          get_role(key_object):Object
add       add_role(object,association_object)   -x-
remove    remove_role(object)                   -x-
replace   -x-                                   replace_role(position,obj
                                                ect)
```

**Figure 14–3: A unidirectional association to many with a restriction at the origin.** *(p. 287)*

> **Diagram content (transcribed from the figure image):** Person 1 —× → * Car (unidirectional to many).

**Figure 14–4: Unidirectional association to 1 with no restrictions at the origin.** *(p. 287)*

> **Diagram content (transcribed from the figure image):** Car * —× → 1 owner Person (unidirectional to one).

The implementation of the Car class requires an instance variable named owner implemented with type Person. Regarding the association methods, following Table 14–2, only getOwner and replaceOwner should be implemented. In the code below, we represent only the lines that are necessary to implement those specific associations. The __init__ method also would have only the necessary arguments to clarify this example by leaving other possible arguments out of the code:

```python
class Car:
    def __init__(self, an_owner):
        self.owner = an_owner
    #ASSOCIATIONS
    def get_owner(self):
        return self.owner
    def replace_owner(self, new_owner):
        self.owner = new_owner
```

In the case of a role with multiplicity 0..1, we must be concerned that there are two possibilities when we get the value of the role: either an object is returned or something else that represents no object is returned. Some languages have null objects that usually are a problem because any message sent to them results in raising an exception.

Woolf (1998) proposed a design pattern named Null object which consists of creating a special object that is interpreted as null but that behaves differently, being capable, for example, to respond to some messages.

Python implements this idea with the object None. It represents “no object,” but you can use it in expressions. Thus instead of returning a set with one element or a set with no element, we can implement returning an object or None. This decision is necessary because, differently to OCL that uses the natural notion of sets, Python uses the mathematical notion of sets, which means that a set that contains one element is different than the element.

If we assume that the role multiplicity in Fig. 14–5 is 0..1, we could then implement the basic methods as with get, add and remove, according to Table 14–2, and the payment must not be informed in the __init__ method.

```python
class Order:
    def __init__(self):
        self.payment = None
    def get_payment(self):
        return self.payment
    def add_payment(self, a_payment):
        self.payment = a_payment
    def remove_payment(self):
        self.payment = None
```

In this example, when an object that already has a payment receives the message add_payment, it will replace the old payment by the new one. This behavior may be defined to be different in other projects, which would, for example, produce an exception or prevent the execution of the operation. Similarly, when an order does not have a payment and the remove_payment is executed, nothing results from that. In other approaches, an exception could be the case in some situations.

### 14.2.2 Unidirectional association to set — 14.2 Unidirectional associations

The unidirectional association to many may be implemented as a collection. If it is a simple association with multiplicity– in the destination role, then it may be implemented as a set. Below is a Python example for the association represented in Fig. 14–6.

```python
class Person:
    def __init__(self):
        self.assessments = set()
    def get_assessments(self):
    return self.assessments
def add_assessment(self, an_assessment):
    self.assessments.add(an_assessment)
def remove_assessment(self, an_assessment):
    self.assessments.remove(an_assessment)
```

As defined in Table 14–2, it must implement the operations get, add, and remove, and no initial value is passed to the __init__ function that just initializes the set of assessments as an empty set.

Here we deal with a set collection that prevents operations such as “get last element” or “get element in position x.” Thus we must deal with the structure with the ways that are proper to it. For example, suppose each assessment has a concluded attribute, as shown in Fig. 14–7.

**Figure 14–5: Unidirectional association to 0..1.** *(p. 289)*

> **Diagram content (transcribed from the figure image):** Order —× → 0..1 Payment (unidirectional to optional).

**Figure 14–6: A unidirectional association to many.** *(p. 289)*

> **Diagram content (transcribed from the figure image):** Person —× → * Assessment.

**Figure 14–7: An evolution of Fig. 14–5.** *(p. 290)*

> **Diagram content (transcribed from the figure image):** Person —× → * Assessment {+concluded: Boolean = False}.

In this case, the class Assessment must provide the methods get and set so that its attribute can be used. As we cannot usually address members of a set by their positions, we usually deal with the whole set at a time. For example, suppose that the class Person has a method to conclude all assessments linked to it. For accessing each element in the set of assessments, an iterator operator will be useful. In this case, we can write a Python expression such as for an_assessment in self.get_assessments(): an_assessment.set_concluded(True). The complete code for both classes is shown below:

```python
class Assessment:
    def __init__(self):
        self.concluded = False
    def get_concluded(self):
        return self.concluded
    def set_concluded(self, a_boolean):
        self.concluded = a_boolean
class Person:
    def __init__(self):
        self.assessments = set()
    def get_assessments(self):
        return self.assessments
    def add_assessment(self, an_assessment):
        self.assessments.add(an_assessment)
    def remove_assessment(self, an_assessment):
        self.assessments.remove(an_assessment)
    def conclude_all_assessments(self): #new delegate method
        for an_assessment in self.get_assessments():
            an_assessment.set_concluded(True)
```

In the new delegate method, we could also write for an_assessment in self.assessments:. It would work the same way. However, even inside the same class, it is preferable to use the method get to access an instance variable than using the name of the instance variable itself. This is because in some cases the get method may execute hidden operations that are necessary.

**Figure 14–8: A model with a bag.** *(p. 291)*

> **Diagram content (transcribed from the figure image):** Product —× → * {bag} viewer Person.

### 14.2.3 Unidirectional to bag — 14.2 Unidirectional associations

Python does not implement any structure like a bag. However, it can be implemented by using a common list as a base and by implementing only get, add, and remove. As stated in Table 14–2 for bags. That is, we are not implementing methods to access an element by its position. Fig. 14–8 shows the base class diagram with a bag and its Python code could be like:

```python
class Product:
    def __init__(self):
        self.viewers = []
    def get_viewers(self):
        return self.viewers
    def add_viewer(self, a_person):
        self.viewers.append(a_person)
    def remove_viewer(self, a_person):
        self.viewers.remove(a_person)
```

### 14.2.4 Unidirectional to sequence — 14.2 Unidirectional associations

The sequence is the most used structure in Python programming although, as seen before, it is relatively rare in the real world. Fortunately, Python implements the sequence structure with the datatype list. Fig. 14–9 shows a situation (list) where a sequence is the right structure to use in the role.

The following code shows the implementation of this role in Python:

```python
class Controller:
    def __init__(self):
        self.qualified_for_gift = []
    def get_qualified_for_gift(self):
        return self.qualified_for_gift
    def get_qualified_for_gift_at(self, position):
        return self.qualified_for_gift[position]
    def add_qualified_for_gift(self, position, a_person):
        self.qualified_for_gift.insert(position, a_person)
    def remove_qualified_for_gift(self, position):
        self.qualified_for_gift.pop(position)
    def replace_qualified_for_gift(self, position, a_person):
        self.qualified_for_gift[position] = a_person
```

### 14.2.5 Unidirectional to ordered set — 14.2 Unidirectional associations

Python also does not implement a structure such as ordered set. There are different ways to implement or simulate this structure. Here we present one of the simplest ones using Python lists to simulate ordered sets. A new class OrderedSet is defined, so that the structure can be reused as if it was a primitive type in Python. Fig. 14–10 shows an structure with an ordered set.

Remind that ordered sets are lists that do not repeat elements but where elements have position. Thus we can create a new class OrderedSet by using a list as a base and controlling duplicates in the methods add_role and replace_role.

By project decision, we must decide how the abovementioned methods behave. For example, if you have an ordered set [5, 2, 8, 9, 4] and you insert the element “8” at different positions, you can have the following results:

- Position 0: [8, 5, 2, 9, 4]

- Position 1: [5, 8, 2, 9, 4]

- Position 2: [5, 2, 8, 9, 4]

- Position 3: [5, 2, 9, 8]

- Position 4: [5, 2, 9, 4, 8]

To obtain these results when an element is inserted into an ordered set, the idea is to check the list and, if the element already is in the list, to delete it from its old position and then insert it in the new position. If the element already appears at the indicated position, nothing needs to be done.

Regarding the replace_role method, the results are not very clear. What if the element already appears in the list; should it be removed before or after the replacement? Let us get again the list [5, 2, 8, 9, 4] and see in Table 14–3 what happens when the repeated element is removed before or after the replacement.

Here we can see that if the element already is in the ordered set, we have different results if the original element is at or after the new position where it will be placed.

We adopt the “before” strategy because it seems more adequate to say that the element in position n will be replaced by a new one. We only must have in mind that if the element already was in the list, then after the replacing operation, it may go to the position n 2 1, and not to n, if the identical element in the least was before the position where the new elements will be placed. This approach also prevents the error that would happen if the element were placed in the last position of the ordered set. Thus if the element is already in the list, we first replace it and then remove the old one, except if the old one is also the replaced one.

**Figure 14–9: A model with a sequence.** *(p. 292)*

> **Diagram content (transcribed from the figure image):** Controller —× → * {sequence} qualified_for_gift Person.

**Figure 14–10: A model with an ordered set.** *(p. 292)*

> **Diagram content (transcribed from the figure image):** Product —× → * {ordered} viewers Person.

**Table 14–3: Different results obtained by replacing a repeated element in an ordered set depending on the positions.**

|**Position**|**Original**|**list** **Insert** **removin** **positio**|**“8” before** **g from the** **n**|**Insert “8” after** **removing from the** **position**|
|---|---|---|---|---|
|0|[5, 2, 8,|9, 4] [**8**, 2,|9, 4]|[**8**, 2, 9, 4]|
|1|[5, 2, 8,|9, 4] [5,**8**,|9, 4]|[5,**8**, 9, 4]|
|2|[5, 2, 8,|9, 4] [5, 2,|**8**, 9, 4]|[5, 2,**8**, 9, 4]|
|3|[5, 2, 8,|9, 4] [5, 2,|**8**, 4]|[5, 2, 8,**8**]|
|4|[5, 2, 8,|9, 4] [5, 2,|9,**8**]|<<index error>>|

Having this into consideration, this would be the Python code for defining the OrderedSet data structure:

```python
class OrderedSet:
    def __init__(self):
        self.representation = []
    def get(self):
        return self.representation
    def get_at(self, position):
        return self.representation[position]
    def add(self, position, object):
        for element in self.representation:
            if element == object:
                self.representation.remove(element)
                break
        self.representation.insert(position, object)
    def remove(self, object):
        self.representation.remove(object)
    def remove_at(self, position):
        self.representation.pop(position)
    def replace(self, position, object):
        self.representation[position] = object
        for index in range(0, len(self.representation)):
            if self.representation[index] == object and index != position:
                self.representation.pop(index)
                break
```

Now we can create a role with {ordered} in any class that would need it. Thus we can write Python code for the role in Fig. 14–10:

```python
import ordered
class Product():
    def __init__(self):
        self.viewers = ordered.OrderedSet()
    def get_viewers(self):
        ordered.get(self.viewers)
    def get_viewers_at(self, position):
        ordered.get_at(self, position)
    def add_viewers(self, position, a_person):
        ordered.add(position, a_person)
    def remove_viewers(self, a_person):
        ordered.remove(a_person)
    def remove_viewers_at(self, position):
        ordered.remove_at(position)
    def replace_viewers(self, position, a_person):
        ordered.replace(position, a_person)
```

### 14.2.6 Unidirectional to array — 14.2 Unidirectional associations

An array is a list with fixed size. Python does not have the array as a built-in data structure, but we can simulate an array by creating a list with a given size, filling it with None’s or zeros, for example, and then not implementing methods that could change the size of the list. Therefore an array will just have the get and replace methods, and its size will always be the same.

An example of an array could be a tray of eggs, as seen in Fig. 14–11. There are always 12 positions to place eggs in a Tray, and some of them can contain an Egg while others contain None.

It is not necessary to use a constraint or stereotype to inform that a given role is an array because its multiplicity will denote that. In the example, the role egg has 12 positions, not more not less.

**Figure 14–11: A model with an array.** *(p. 294)*

> **Diagram content (transcribed from the figure image):** Tray 0..1 —× → 12 Egg (fixed multiplicity → array).

When we define a role as an array, the number of positions must be informed when the object is instantiated. Therefore the method __init__ would receive the size of the array as a parameter. The code blow represents the class Tray with the array representation with 12 spaces, numbered from 0 to 11, that can contain an Egg or None:

```python
class Tray():
    def __init__(self, size):
        self.representation = []
        for i in range(size):
            self.representation.append(None)
    def get_eggs(self):
        return self.representation
    def get_egg_at(self, position):
        return self.representation[position]
    def replace_egg_at(self, position, an_egg):
        self.representation[position] = an_egg
```

### 14.2.7 Unidirectional qualified association — 14.2 Unidirectional associations

The unidirectional qualified association is implemented like the association with multiplicity to many. However, instead of the data type set, we use a mapping, or dictionary structure (dict) that associates an alphanumeric, primitive, or enumeration type (key) to one object or a set of objects (values).

As for any other unidirectional associations, we must keep in mind that the unidirectional implementation is only possible when the association has no multiplicity bounds in its origin, that is, the origin role must have multiplicity– . If this is not the case, a bidirectional implementation must be considered.

Fig. 14–12 shows a model with a qualified association defining a map to 0..1 with an internal qualifier. When the qualifier is internal, it does not need to be passed as argument in the add method, because the value is already stored in the object. The Python code would be like this:

```python
class Person():
    def __init__(self):
        self.phones = dict()
    def get_phones(self):
        return self.phones
    def get_phone_at(self, key):
        return self.phones[key]
    def add_phone(self, a_phone):
            self.phones[a_phone.get_number()] = a_phone
    def remove_phone(self, a_phone):
        self.phones.pop(a_phone.get_number())
    def remove_phone_at(self, a_key):
        self.phones.pop(a_key)
```

**Figure 14–12: A model with a qualified association with internal qualifier.** *(p. 296)*

> **Diagram content (transcribed from the figure image):** Qualified map: Person with qualifier number —× → 0..1 Phone {«imm» «unique» +number: PhoneNumber}.

The replace method is not implemented in this case because it would not make sense to replace an object with a unique attribute in a dictionary that uses that same attribute as qualifier.

It is important to stress that the design of the qualified association with an internal qualifier works better if the qualifier attribute is immutable. If this was not the case, the attribute could change, and that change would not necessarily propagate to the value that is the key for the association. This would create an inconsistency. That constraint, however, does not apply to maps with external qualifiers, because in that case the qualifier is not an attribute of the qualified class.

Fig. 14–13 presents a map with an external qualifier. The corresponding code is shown below:

```python
import phone
class Person():
    def __init__(self):
        self.phones = dict()
    def get_phones(self):
        return self.phones
    def get_phone_at(self, a_key):
        return self.phones[a_key]
    def add_phone(self, a_key, a_phone):
        self.phones[a_key] = a_phone
    def remove_phone(self, a_phone):
        for key in self.phones.keys():
            if self.phones[key] == a_phone:
                self.phones.pop(key)
                break
    def remove_phone_at(self, a_key):
        self.phones.pop(a_key)
    def replace_phone(self, a_key, a_phone):
        self.phones[a_key] = a_phone
```

In the case of Fig. 14–13, there is an issue to be considered: as the origin of the association has no multiplicity restriction, and the qualifier is not an attribute of the class, nothing assures that the same phone is not associated to two or more keys. For example, the following sequence of commands would produce a phone associated to two different types: 

```text
a_person.add_phone(“residential”, a_phone)
a_person.add_phone(“comercial”, a_phone)
```

**Figure 14–13: A model with an external qualifier.** *(p. 297)*

> **Diagram content (transcribed from the figure image):** Qualifier by enumeration: Person with type:PhoneType —× → 0..1 Phone {«imm» «unique» +number}; «enumeration» PhoneType {mobile, home, work}.

If that is what is expected, nothing else must be said. But if that does not agree with the business rules, then the role on the left side should be 1 and the association should be implemented as a bidirectional association, so that control mechanisms could avoid a phone from being associated to more than one type.

Now, let us see the case of unidirectional qualified association that is the “partition” (relations must be bidirectional) with internal qualifier. For the next example, we consider that a person may have a set of phones for each type (Fig. 14–14). And the Python code for the qualified role is:

```python
class Person():
    def __init__(self):
        self.phones = dict()
    def get_phones(self):
        return self.phones
    def get_phones_at(self, a_key):
        return self.phones[a_key]
    def add_phone(self, a_phone):
        key = a_phone.get_idd()
        if not key in self.phones.keys():
            self.phones[key] = set()
        self.phones[key].add(a_phone)
    def remove_phone(self, a_phone):
        for key in self.phones.keys():
            if a_phone in self.phones[key]:
                self.phones[key].remove(a_phone)
                if len(self.phones[key]) == 0:
                    self.phones.pop(key)
                    break
```

**Figure 14–14: A model with a partition and an internal qualifier.** *(p. 298)*

> **Diagram content (transcribed from the figure image):** Partition: Person with qualifier idd —× → * Phone {«imm» +idd: IDDNumber; «imm» «unique» +number: PhoneNumber}.

**Figure 14–15: A model with a partition with external qualifier.** *(p. 298)*

> **Diagram content (transcribed from the figure image):** Person with type:PhoneType —× → * Phone; «enumeration» PhoneType {mobile, home, work} (relation/multimap).

Finally, if the partition has an external qualifier as seen in Fig. 14–15, the code would be like:

```python
class Person():
    def __init__(self):
        self.phones = dict()
    def get_phones(self):
        return self.phones
    def get_phones_at(self, a_key):
        return self.phones[a_key]
    def add_phone(self, a_key, a_phone):
        if not a_key in self.phones.keys():
            self.phones[a_key] = set()
        self.phones[a_key].add(a_phone)
```

### 14.2.8 Unidirectional association with association class — 14.2 Unidirectional associations

When the association has an association class, it is necessary to implement the creation and destruction of instances of that class each time a corresponding link is added or removed.

Association classes may exist in associations with any multiplicity. However, they are more common and useful in associations that are many to many.

One possible implementation for this kind of association is to create a dict associating instances of the opposite class to instances of the association class.

**Figure 14–16: A model with an association class.** *(p. 299)*

> **Diagram content (transcribed from the figure image):** Person —× → * Organization with association class Job.

Fig. 14–16 shows an association class, and its implementation is shown below:

```python
from job import Job
class Person():
    def __init__(self):
        self.organization_job = dict()
    def get_organizations(self):
        return set(self.organization_job.keys())
    def get_jobs(self):
        return set(self.organization_job.values())
    def get_job_at(self, an_organization):
        return self.organization_job[an_organization]
    def add_organization(self, an_organization):
        new_job = Job()
        self.organization_job[an_organization] = new_job
    def remove_organization(self, an_organization):
        self.organization_job.pop(an_organization)
```

In Fig. 14–16, we see that when a new link is created from Person to Organization with add_organization, a new instance of Job is automatically created.

As Python has garbage collector, it is not necessary to explicitly destroy the instance of Job in remove_organization, but some care must be taken to confirm whether there are no other classes with mandatory associations to the association class.

## 14.3 Bidirectional associations

*Chapter 14 · p. 299*

As mentioned before, the unidirectional implementation of associations is only possible when they are navigable in one direction and there is no multiplicity constraint in the origin role. In other situations, the bidirectional implementation is necessary.

At least three patterns for implementing bidirectional associations have been proposed (Fowler, 2003):

- Implementing the association as two unidirectional associations (mutual friends).

- Implementing the association as a unidirectional association in just one of the classes, and making navigation to the opposite side be done over a derived association.

- Implementing an intermediary object that represents the association.

In all the cases above, if the association is navigable in both directions, the get method must be implemented in both participating classes, because navigation must be allowed in both directions. However, if we have the case of a unidirectional association with a multiplicity restriction at the origin, then the get method must be implemented only at the origin class.

The add, remove, and replace methods, if required, may be implemented only in one of the classes, because if they exist in both classes, they would be redundant as they would do the same thing.

### 14.3.1 Mutual friends — 14.3 Bidirectional associations

The option for implementing bidirectional associations in both directions is the best in terms of time efficiency, but it is less efficient in terms of space allocation because each association is implemented twice. It may also require more control overhead because the implementation of the association in both classes must be synchronized.

The implementation of the unidirectional components of the association follows the recommendations given before.

If both roles are optional and no other constraints are present, then links may be added and removed at will. Otherwise, care must be taken not to violate structural rules. As links must be added and removed from both sides of the association, auxiliary methods would be needed to add and remove the individual unidirectional links in one of the classes.

These auxiliary methods must not be called in any other place except the add and remove methods. That is why they must be declared as private, but the opposite class must have access to them; thus, they are exported exclusively to that class.

Fig. 14–17 presents a bidirectional many-to-many association, and the corresponding implementation code is shown below:

**Figure 14–17: A model with a bidirectional association with no restrictions.** *(p. 300)*

> **Diagram content (transcribed from the figure image):** Bidirectional many-to-many: Person * wishers — * wishes Product.

```python
class Person():
    def __init__(self):
        self.wishes = set()
    def get_wishes(self):
        return self.wishes
    def add_wish(self, a_product):
        self.wishes.add(a_product)
        a_product._add_wisher(self)
    def remove_wish(self, a_product):
        self.wishes.remove(a_product)
        a_product._remove_wisher
class Product():
    def __init__(self):
        self.wishers = set()
    def get_wishers(self):
        return self.wishers
    def _add_wisher(self, a_person):
        self.wishers.add(a_person)
    def _remove_wisher(self, a_person):
        self.wishers.remove(a_person)
```

The methods _add_wisher and _remove_wisher implemented in class Product are considered as protected and must not be used by other methods besides the ones they were designed to. Python does not have real protected methods. Thus programmers usually prefix the name of the method with “_” to indicate that it is protected.

As mentioned before, the access methods (get) must be implemented in both classes if the association is navigable in both directions. But the add and remove methods may be implemented in just one class. In the example above, they are implemented only in class Person.

In any case, one class implements the add and remove methods and the other implements the auxiliary protected methods _add and _remove.

### 14.3.2 Unidirectional implementation — 14.3 Bidirectional associations

Even if the association is bidirectional, it may be the case that navigation occurs much more often or is more critical in just one direction. If that happens, an option is to implement the association physically in only one direction and implement the get method for the opposite side as a derived association. The advantage is that the code is simpler, faster in one direction, and space saving. The disadvantage is that the navigation from the opposite direction would be much slower.

**Figure 14–18: Representation and implementation of a bidirectional association with unidirectional implementation.** *(p. 302)*

> **Diagram content (transcribed from the figure image):** Bidirectional association Person * tutors — * pets Pet implemented as one real one-way association Person → * pets Pet plus a derived inverse /tutors (Pet → Person).

This form of implementation is also easier when the role on the origin of the implemented direction has no multiplicity restriction. If there is a restriction, then the unidirectional implementation is possible only if additional mechanisms to control multiplicity at the origin of the association are implemented, with more loss of performance. Fig. 14–18 shows an example of a bidirectional association (upper) and its implementation as a normal unidirectional association from Person to Pet and a derived association from Pet to Person.

Observe that the lower part of the figure represents the design implementation of the conceptual upper part of the figure. In the lower part, navigation from Pet to Person is only possible through the derived association/tutors; pets is not navigable. ON the other hand, navigation from Person to Pet is only possible through the unidirectional association with role pets, and which is not navigable to the other sense. The Python code would be the following:

```python
Class Person():
    def __init__(self):
        self.pets = set()
    def get_pets(self):
        return self.pets
    def add_pet(self, a_pet):
        self.pets.add(a_pet)
    def remove_pet(self, a_pet):
        return self.pets.remove(a_pet)
from person import Person
class Pet:
    def __init__(self):
        pass
    def get_tutors(self):
        all_persons = Person.all_instances()
        tutors = set()
        for person in all_persons:
            if person in self.get_tutors():
                tutors.add(person)
        return tutors
```

Python does not implement the function all_instances and many consider it as an antipattern. Thus maybe this is not really the best choice for implementing bidirectional associations.

### 14.3.3 Association proxy — 14.3 Bidirectional associations

A bidirectional association may also be implemented by means of an intermediary object that represents the association. The intermediary object consists of a class that represents a table with pairs of linked instances. This table is highly reusable. First, there will be slightly different implementations for the table depending on the multiplicity and other restrictions in roles. Let us see one possible implementation for a– to– bidirectional association:

```python
table = dict()
def create(name):
    table[name] = []
    return table[name]
def link(a, name, b):
    table[name].append((a, b))
def unlink(a, name, b):
    table[name].remove((a, b))
def get_from_key(name, key):
    result = set()
    for pair in table[name]:
        if pair[0] == key:
            result.add(pair[1])
    return result
def get_from_value(name, value):
    result = set()
    for pair in table[name]:
        if pair[1] == value:
            result.add(pair[0])
    return result
```

After trying and studying diverse forms of implementation of the association proxy, the simpler form seems to be implementing it as a global variable that contains a dictionary that relates names of associations (role1_role2) to a list of pairs that represent the linked elements. The methods in this case are all static.

This solution could be used in cases like the one in Fig. 14–18 to represent the bidirectional association that is completely balanced in terms of execution time relative to its roles. The get methods must be implemented in both classes while add, remove, and replace only in one class. This is the code of the class Person that uses the Association Proxy to implement all methods for association wishers_wishes between classes Person and Product: 

```python
import association
WW = ‘wisher_wish’
class Person():
    def __init__(self):
        if not WW in association.table.keys():
            association.create(WW)
    def get_wishes(self):
        return association.get_from_key(WW, self)
    def add_wish(self, a_product):
        association.link(self, WW, a_product)
    def remove_wish(self, a_product):
        return association.unlink(self, WW, a_product)
    def remove_wish(self, a_product):
        return association.unlink(self, WW, a_product)
```

The code for the other participating class is simpler:

```python
import association
WW = ‘wisher_wish’
class Product():
    def __init__(self):
        if not WW in association.table.keys():
            association.create(WW)
    def get_wishers(self):
        return association.get_from_value(WW, self)
```

Care must be taken to use the same name for the association in both classes. In order to avoid repeating the string “wisher_wish” many times, a constant WW was defined to be used in its place.

For a second association in the same class, a new association name must be created and the methods get, add, and remove implemented for this specific association in both participating classes.

That leads to the temptation of changing methods like add_wisher(self, a_product) by add (self, “wisher,” product). In this case, a lot of methods would not be written, but only if they conform to the general form. Any different configuration of multiplicity or constrains in the roles would need a different table structure.

The association proxy approach tends to be much simpler and maintainable than the former ones. It also mimics the structure of a relational database because associations are indeed implemented as intermediary tables, which correspond to the intermediary object here.

The disadvantage of this method is that getters are slower in both directions when compared to the bidirectional approach and the global visibility of the intermediary object may cause design hazards if not used carefully.

## 14.4 Delegated methods and system operations

*Chapter 14 · p. 305*

To this point, we have shown how to generate code for classes, attributes, associations, and their corresponding basic methods that may be considered part of their basic structure. Now it is the time to explain how to implement delegate methods and system operations. These should be implemented by following the dynamic models explained before.

In a system sequence diagram, system operations are implemented as a sequence of messages that are sent by the controller. Some of those messages could be basic operations so that their code is already known, as explained by the patterns in this chapter. However, some messages are not basic, but delegate, and they have to be discovered and implemented considering the sequence of messages that are sent by the same object that received the delegate method in continuation for this.

Let us look again at Figure 13–28, reproduced here as Fig. 14–19.

In this diagram, we observe five basic operations: get_proposals and get_person, that are basic queries on roles from: Controller to itself. On the other hand, send_proposal is a system operation that is usually delegated, and create_new_sending is a delegate message from: Controller to a_proposal.

Let us forget for now the basic operations and deal with the implementation of those two nonbasic messages. First, the send_proposal system operation should be implemented in class Controller as a sequence of messages that directly follow it in the sequence diagram considering just one level in deepness. This means that send proposal will not be implemented as:

**Figure 14–19: A sequence diagram with the model of a system operation.** *(p. 305)*

> **Diagram content (transcribed from the figure image):** Sequence diagram for send_proposal used to generate code (same as Fig 13–28): Interface → Controller send_proposal(a_proposal_id, a_federal_manager_id); Controller: a_proposal = get_proposals(a_proposal_id); a_federal_manager = get_person(a_federal_manager_id); Controller → a_proposal create_new_sending(a_federal_manager); Proposal creates new_sending : Sending, add_sending(new_sending), new_sending.add_federal_manager(a_federal_manager).

1. get_proposals

2. get_person

3. create_new_sending

- 3.1 new_sending

- 3.2 add_sending

- 3.3 add_federal_manager

The implementation of the messages at the second level (3.1, 3.2, and 3.3) is delayed. Instead of that, only the three messages at the first level after send_proposal are implemented:

1. get_proposal

2. get_person

3. create_new_sending

The other messages from Proposal to Sending and Proposal to Proposal are sent from a_proposal to new_sending and a_proposal in the implementation of the delegate method create_new_sending:

1. Create

2. add_sending

3. add_federal_manager

It would be a problem if messages from different levels were mixed in the same method implementation. For example, if the Create() message to sending was implemented inside method send_proposal, a problem of cohesion would arise, as seen before.

That said, the code for the system and delegate methods in the diagram (ignoring other basic methods for now) could be:

```python
class Controller:
    #...
    def send_proposal(self, a_proposal_id, a_federal_manager_id): #SYSTEM OPERATION
        a_proposal = self.get_proposals(a_proposal_id)
        a_federal_manager = self.get_person(a_federal_manager_id)
        a_proposal.create_new_sending(a_federal_manager_id)
class Proposal:
    #...
    def create_new_sending(self, a_federal_manager):     #DELEGATE METHOD
        new_sending = Sending()
        self.add_sending(new_sending)
        new_sending.add_federal_manager(a_federal_manager)
```

As it can be seen, this implementation avoided increasing coupling because it does not return the new Sending to the controller. Instead of concentration, this code works with delegation.

## Questions (Chapter 14)

1. Explain in detail how a delegate message that appears in a sequence diagram must be implemented.

2. What are the basic operations that must be implemented for most kinds of associations? 3. Considering Fig. 13-26, a Proposal has an association to Sending that is 1 to– {ordered}{ stackc. Considering that this association is bidirectional, show the mutual-friends implementation of its representation and its methods.

4. Consider Fig. 13-28, try to present a concentration version of this diagram and present the corresponding (smelling) code.

5. Produce a design domain version of the classes in Fig. 12-7.

This page intentionally left blank

