<!-- Knowledge file: Chapter 15 — Testing -->
> **About this file.** Chapter 15 of a cleaned, AI-ready edition of Wazlawick, R. S. (2024). Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-443-13739-6.  
> **Covers:** Testing: functional tests derived from use cases and contracts, unit tests, stubs and drivers, test-driven development, acceptance tests.  
> **Use this file when:** designing test cases from use cases/OCL contracts or doing TDD.  
> **Sections:** 15.1 Introduction to testing (p. 307); 15.2 Functional testing (p. 310); 15.3 Stubs (p. 312); 15.4 Drivers (p. 314); 15.5 Test-driven development (p. 318); 15.6 Unit testing with TDD (p. 318); 15.7 Use case testing (p. 327)  
> **Contains:** 2 figures transcribed as text, 24 code listings.

# Chapter 15: Testing

*Source: Wazlawick, Object-Oriented Analysis and Design for Information Systems, 2nd ed. (Elsevier, 2024), starts p. 307*

## Key topics in this chapter (Chapter 15)

- Functional testing

- Stubs and drivers

- Test-driven development

- Unit testing

- System testing with use cases

## 15.1 Introduction to testing

*Chapter 15 · p. 307*

No matter how sophisticated the modeling and specification techniques used to develop software are, no matter how disciplined and competent the team is, there is a factor that makes software testing always necessary: human error. It is a myth to think that good developers working with state-of-the-art tools are capable of developing error-free software (Beizer, 1990).

Murphy’s Law (Bloch, 1980) in many of its corollaries seems to speak directly to the software industry. For example:

- Anything that can go wrong will go wrong (at the worst time ever).

- If everything seems all right, you have not checked appropriately.

- Nature always sides with the hidden flaw.

For many years, software-testing activities were considered a punishment to programmers. Testing was considered as a waste of time because software was supposed to be correct from the beginning.

However, things have changed. The test discipline now is considered extremely important. Today, it is an integral part of the software development process and one of the most fundamental disciplines in software engineering.

Furthermore, leading software development companies started to outsource software testing, by hiring test factories. That means that not only developers but also teams are especially trained to conduct testing.

This chapter presents test activities that are strongly adapted for use with the techniques shown in previous chapters. In special, this chapter will deal with two important levels of test: unit tests and system tests.

Unit tests are used basically to check the behavior of classes, including their basic and delegate methods. If automatic code generation is used, such tests may be suppressed, because it is assumed that automatic code generators do not make human errors. 

309 

On the other hand, system tests can be performed as systematic use case tests. Each use case is a script that establishes normal and alternate flows for accomplishing business goals. Use case tests also may be executed manually or automatically. If the client executes use case tests following the system tests proposed, then they are called acceptance tests.

There are two major categories of test techniques:

- Structural tests, which evaluate the internal structure of the code.

- Functional tests, which evaluate operations based only on their inputs and outputs.

In this book, only functional techniques applied specifically to the two levels of testing mentioned are introduced:

- Functional unit test applied to any kind of methods, but especially to system operations, which already have contracts that ease the process of identifying the test cases.

- System tests based on system use cases. This kind of test has variants. If conducted by final users, they are acceptance tests. As the development team gives the user more proactivity and less control during the tests, they can also be called α or β tests.

Meszaros (2007) and Beck (1989) are good references to understand automated tests and its patterns.

## 15.2 Functional testing

*Chapter 15 · p. 310*

Functional testing consists of a sequence of tests that define entry values for an operation and observe if the result is what was expected. Functional tests may be run without any knowledge of the programming code that implements the operation; only its behavior is observed. The quantity of tests to be conducted to assure that an operation is correct may be virtually undefined. However, functional testing may use techniques to reduce the number of necessary tests without losing coverage. The most useful techniques for accomplishing that goal are equivalence partitioning and limit value analysis, which are explained in the following subsections.

### 15.2.1 Equivalence partitioning — 15.2 Functional testing

One of the principles of functional testing is the identification of equivalent situations. For example, if an operation accepts a set of data (normality) and rejects another set (exception), then it may be said that there are two equivalence classes^1 of input data for that operation: accepted and rejected values. It is usually impossible to test every value included in those classes, because they may be virtually infinite. Thus the technique of equivalence partitioning indicates that at least one element in each equivalence class must be tested (Burnstein, 2003).

> *Footnote 1:* As literature usually uses the term equivalence classes, which is a mathematical concept, to refer to the set of objects than can or cannot be accepted, the reader must avoid confusing them with classes from the conceptual or domain models.

Classically, the equivalence partitioning technique considers the division of the inputs through the following criteria (Myers et al., 2004):

- If the valid values are specified as an interval (e.g., from 10 to 20), then we define one valid class (10 to 20) and two nonvalid classes (less than10 and more than 20).

- If the valid values are specified as a quantity of values (e.g., a list with five elements), then we define a valid class (list with five elements) and two nonvalid classes (lists with less than five elements and lists with more than five elements).

- If the valid entries are specified as a set of acceptable values that may be processed in different forms (e.g., the strings of an enumeration such as “adult” and “minor”), then we define a valid class for each of the valid options and an invalid class for all other values.

- If the valid values are specified by a logical condition (e.g., a comparison between dates: “today must be greater than birth date”), then we must define a valid class (when the condition is true. E.g., today 5 07/12/2023 and birthday 5 09/29/1967) and an invalid class (when the condition is false; e.g., today 5 07/12/2023 and birthday 5 03/22/2233). Consider dates being represented as MM/DD/YYYY.

The classes of valid inputs may be defined not only in terms of restrictions on the input data but also in terms of the results that may be produced. If the operation that is being tested has different behavior depending on the value of the input, then different valid sets must be defined for each behavior. For example, consider a simple operation half(x:Integer):Integer. Business rules state that this operation accepts only positive numbers for x. Thus the operation is defined to fail if trying to accept zero or negative numbers. Finally, consider that the operation produces (x 2 1)/2 for odd numbers and x/2 for even numbers (the results also belong to the domain of Integer). Thus we must consider that half has three equivalence classes for the parameter x:

- A valid class composed of odd positive integers: 1, 3, 5, . . .

- A valid class composed of even positive integers: 2, 4, 6, . . .

- An invalid class composed of nonpositive integers: 0, 21, 22, 23, . . .

The equivalence class values must be always restricted to the domain defined by the type of the parameter. For example, if the type of the parameter were something other than Integer, then different equivalence classes would be defined. If the operation was half(x:Natural):Integer, then the equivalence classes should be redefined so that they remain inside the Natural domain, which does not include zero and negative numbers:

- A valid class composed of odd Naturals: 1, 3, 5, . . .

- A valid class composed of even Naturals: 2, 4, 6, . . .

- No invalid classes.

On the other hand, assume the operation is defined with a broader parameter type such as half(x:Float):Integer; then the equivalence classes would be:

- A valid class composed of odd positive integers: 1, 3, 5, . . .

- A valid class composed of even positive integers: 2, 4, 6, . . .

- An invalid class composed of positive nonintegers: 0, 3.1, 4.5, 17.334, 0.003, . . .

- An invalid class composed of negative float or integer numbers: 23, 28, 24.1, 217.6, 2100, ...

We can see from the examples above that if the designer restricts the type of the parameter as much as possible (using Natural instead of Integer or Float in this example), then fewer or simpler invalid equivalence classes would be defined. That is why examples in previous chapters use the Natural type instead of Integer whenever zero or negative numbers could not be accepted. And that is why enumerations should be used rather than unrestricted strings whenever possible. Having less classes to test contributes to agility.

### 15.2.2 Limit value analysis — 15.2 Functional testing

People who work in software testing used to say that (software) bugs hide in the slits. Due to this, the equivalence partitioning technique is often used in conjunction with another technique known as limit value analysis.

Limit value analysis consists of avoiding choosing random values from an equivalence class but choosing one or more limit values if they can be determined.

In those domains, such as numbers, this criterion may be applied. For example, if an operation requires an integer parameter that is valid only if included in the interval [10..20], then there are three equivalence classes:

- Invalid for any x , 10.

- Valid for x $ 10 and x # 20.

- Invalid for any x . 20.

Limit value analysis suggests that eventual errors in the logic of a program do not happen at random places in the code, but they concentrate at the boundary points where two intervals of data meet. Thus if the domain of the parameter is Integer:

- For the first invalid class, the value 9 must be tested.

- For the valid class, 10 and 20 must be tested.

- For the second invalid class, the value 21 must be tested.

Thus if there is a logic error in the operation for some of these inputs, it is much more probable that it will be found in this way rather than if a random value is chosen inside each interval that defines an equivalence class.

## 15.3 Stubs

*Chapter 15 · p. 312*

Frequently, parts of the software must be tested apart from the main body of code, but at the same time, they must communicate with those other parts.

Let us get one example from combinatorics. If you are familiarized with the concepts of factorial and combination, you will understand easily. When a method combination (that is going to be tested) needs to call operations such as factorial that has not yet being implemented, then the component factorial may be replaced by a simplified version of it that implements only the behavior that is necessary to perform the test of combination operation. This simplified component that is used in the place of a component that has not yet been implemented is called a stub.

For example, suppose that a method combination needs a factorial calculator that has not yet been implemented. A simplified version of factorial may be implemented just for allowing the method combination to be tested. Suppose that given the formula C(n, p) 5 n!/(p!(n 2 p)!) with p # n, we decided to test combination with the following values:

- C(0, 0) 55 1

- • C(1, 0) 55 1 • C(1, 1) 55 1 • C(2, 0) 55 1 • C(2, 1) 55 2 • C(2, 2) 55 1 • C(3, 0) 55 1

- C(3, 1) 55 3

- C(3, 2) 55 3

- C(3, 3) 55 1

In this case, we would be testing the limit value (0, 0) and some additional values. Notice that in order to test combination with those values, we do not need a factorial calculator; we just need to know the values of 0!, 1!, 2!, and 3!. Thus the stub StubFactorial defined below must be enough for this purpose. The name of the file that will contain the following code could be stub_factorial.py, but it implements the method factorial with the same name as in the definitive class to simplify refactoring when the stub is finally replaced by the definitive class.

```python
def factorial(a_natural):
    if a_natural == 0:
        return 1
    elif a_natural == 1:
        return 1
    elif a_natural == 2:
        return 2
    elif a_natural == 3:
        return 6
    else:
        return None
```

In this way, the operation combination may be tested without investigating and defining a possibly more complex operation to calculate factorials.

```python
from stub_factorial import factorial
def combination(n, p):
    return factorial(n) / (factorial(p) * (factorial(n-p)))
```

from stub_factorial import factorial

If we run the tests with the values above for C(n,p), we will see that they are correct.

Although stubs may be considered as mock-ups and therefore disposable after the real component is implemented, it could be a good idea to maintain stubs in a components library. That could accelerate the testing of the class that uses the stub. Imagine that the stub usually will have a few lines of code and use little memory, while the real class that the stub represents may be linked to a series of other classes that may include many lines of code as well as a large testing database. In this case, stubs would be the fastest option to test the original class.

Stubs are useful especially if top-down development happens; but, as we have seen, in other situations too.

## 15.4 Drivers

*Chapter 15 · p. 314*

If the relation of a class and a stub is represented as class ! stub because the class calls for methods implemented in the stub, then another way to address this relation is by using drivers. The relation between a driver and a class that implements the methods that the driver will call may then be driver ! class.

Thus, one use for drivers is to allow bottom-up development similarly as stubs do with top-down. However, drivers may be a much more powerful tool if we implement them systematically. The idea is to make a driver calling a given function for any valid or invalid equivalence class in its parameters. In this way, the driver will be an automatic tester for a given method or class.

In our first example, shown in Fig. 15–1, the element chosen to be tested is the method get_age() in class Person. We will proceed here with the simplest way of testing it so that the idea can be better understood without the introduction of more complex structures.

The class Person has only two attributes: name, and date_of_birth, and four methods, Person(), the constructor, get_name() and set_name(), the basic methods for the attribute name, and a derived method get_age(), which returns the age, in years calculated from the date_of_birth and today. The date_of_birth attribute is immutable and private, but, combined with the date of today, it can allow to derive the age of the person.

Of course, there are algorithms already implemented in Python for calculating age from date of birth, but the idea here is to show a sequence of commands programmed to do this calculation with one mistake placed on purpose, just to see if the test can detect it. 

```python
from datetime import *
class Person:
    def __init__(self, a_name, a_date_of_birth):
        self.name = a_name
        self.date_of_birth = a_date_of_birth
    def set_name(self, a_name):
        self.name = a_name
    def get_name(self):
        return self.name
    def get_age(self):
        today = datetime.date.today()
        t_day = today.day
        t_month = today.month
        t_year = today.year
        b_day = self.date_of_birth.day
        b_month = self.date_of_birth.month
        b_year = self.date_of_birth.year
        age = t_year - b_year - 1
        if t_month > b_month:
            age = age+1
        elif t_month == b_month and t_day > b_day:
            age = age+1
        return age
```

**Figure 15–1: A fragment of a model to be used as example in this section.** *(p. 314)*

> **Diagram content (transcribed from the figure image):** Class to be tested: Person {-name: String; -date_of_birth: Date; +Person(a_name: String); +get_name(): String; +set_name(a_name: String); +get_age(): String}.

To systematically test the get_age() method, we will write a driver for it. The driver is a sequence of tests where we are supposed to at least apply the techniques of equivalence partitioning and limit value analysis seen before in this chapter.

Despite the get_age() method not having any explicit parameter, it has an implicit one, which is the date of today and a private attribute date_of_birth that is used to calculate the age of the person.

Considering the two techniques explained before, we could think of testing the following values:

- An aleatory date in the past (andrew).

- A person who is going to celebrate birthday tomorrow (beth).

- A person who is celebrating birthday today (charles).

- A person who is celebrating 1 year tomorrow (daisy).

- A person who is celebrating 1 year today (edward).

- A person born today (florence).

- A person who will be born tomorrow (gerald). An invalid class—all other classes are valid.

The following is the code that creates the fixtures, that is, objects that will be used exclusively in the driver to test the different equivalence classes. For now, we ignore gerald on purpose because it belongs to an invalid equivalence class and should be tested differently from the other values. 

```python
from person import *
from datetime import *
andrew = Person("Andrew", date(1967, 9, 29))  # YYYY/MM/DD
beth = Person("Beth", date(1980, 8, 10))
charles = Person("Charles", date(1980, 8, 9))
daisy = Person("Daisy", date(2022, 8, 10))
edward = Person("Edward", date(2022, 8, 9))
florence = Person("Florence", date(2023, 8, 9))
gerald = Person("Gerald", date(2023, 8, 10))
```

After creating the fixtures, the sequence of tests is defined. In this case, each assert is a command that compares the result of the method get_age() for the different objects in different equivalence classes with the expected result:

#### 

```text
# today = 08/09/2023
assert(andrew.get_age() == 55)
assert(beth.get_age() == 42)
assert(charles.get_age() == 43)
assert(daisy.get_age() == 0)
assert(edward.get_age() == 1)
assert(florence.get_age() == 0)
```

After running the driver, we obtain the following output:

```text
Traceback (most recent call last):
  File "D:/…/diver_person.py", line 17, in <module>
    assert(charles.get_age() == 43)
AssertionError
Process finished with exit code 1
```

Thus there is something wrong with the age of charles. If we examine the code, we will see that the function get_age() is returning 42 instead of 43 for charles, which is an error because he is celebrating birthday today and 43 would be the right sum. This error is caused by a line in the original file person.py that mistakenly used the “ . ” comparator instead of “ . 5 .” To be more specific, the error is in the line that starts with “elif” in get_age(). Thus in order to fix the mistake, the line:

```text
elif t_month == b_month and t_day > b_day:
```

must be replaced by:

```text
elif t_month == b_month and t_day >= b_day:
```

After correcting this error, the function get_age() will pass in all tests. But we still have the problem with gerald. As future birthdays are not allowed in most systems, they belong to an invalid class of unborn people. In the case of an operation receiving or returning values from invalid classes, many different things could happen. Suppose that in this case we want the get_age() method to raise an exception. Then, the driver, when finding such a situation, should detect this exception, or else, the test is failure.

Thus we can use the following code to finish this driver where we try to execute get_age() over gerald:

```text
try:
    assert(gerald.get_age())
    print("Error: exception not detected")
    raise Exception
except:
    print('pass')
```

If the function get_age() stops with an exception for gerald, then the driver will consider that the test succeeded. However, if the expression gerald.get_age() runs without an exception, then the driver will consider that the test failed, and we obtain the following result:

```text
Error: exception not detected
Process finished with exit code 0
```

The problem of future dates being registered, however, does not start with the method get_age(). In fact, when the instance of Person is created, it should already detect that the date passed as argument is not valid. Thus instead of checking for this problem in method get_age(), it would be better to test it in the __init__ method of Person. An assert that the argument date_of_birth is equal or past today will then be used in this method, and unborn people would not even be created:

```python
class Person:
    def __init__(self, a_name, a_date_of_birth):
        assert a_date_of_birth <= datetime.date.today()
        self.name = a_name
        self.date_of_birth = a_date_of_birth
```

Thus stubs and drivers are simple implementations that simulate the behavior of other components. The stub is used in the place of a component that should be called but is not yet implemented. The driver is used in the place of a component that should call the component to be tested in a systematic and reproducible way.

Both stubs and drivers must be maintained as code assets, the first to avoid the developer to load many classes to test a simple operation and the other to allow the developers to systematically test their code in an automatic way.

## 15.5 Test-driven development

*Chapter 15 · p. 318*

Test-driven development or TDD (Beck, 2003) is a technique and a programming philosophy that incorporates automatic testing to the process of producing code. It works like this:

1. First, the programmer that receives the specification of a new functionality that must be implemented should create or modify a set of automatic tests for the code that does not yet exist or that are now anymore correct, respectively.

2. This set of tests must be executed and observed to fail. This is done to show that the tests won’t succeed unless a new feature is implemented in the code. If the test passes at this time, there are two explanations: either the test is badly written or the feature that is being tested is already present in the code.

3. After the tests fail, the code must be developed with the only objective being passing the tests. (If any other feature is identified by the team, then the tests must be updated before this new feature is introduced in the code. In that case, the process restarts from step 1.)

4. After the code passes all tests, it must be cleaned and improved if necessary, in order to meet internal quality standards. After passing the final tests, it is considered stable and may be integrated into the main body of code of the system.

The contracts that were developed with OCL and the dynamic models in system sequence diagrams are exceptional sources of information for developing complete and consistent test cases before producing any code.

The motivation for TDD is to incentivize the programmer to keep the code simple and to produce a test asset that allows any part of the system to be automatically tested.

## 15.6 Unit testing with TDD

*Chapter 15 · p. 318*

Unit tests are the most elementary tests and consist of verifying if an individual component of the software was implemented correctly. Usually, a test case will verify all conditions for a given method in a class. Let us use a version of the class Person depicted in Fig. 15–2 where the age attribute was used instead of birthday. In this case, age is immutable. This is a situation that is common in some systems when you need to know the age of the person on the date of her registration and not the updated age of today.

**Figure 15–2: A new version of Person to be tested.** *(p. 318)*

> **Diagram content (transcribed from the figure image):** Test driver: «driver» DriverOfPerson —× → 1 Person {«imm» «unique» -id: PersonId = IdGenerator.next(); -name: String; «imm» -age: Natural; -/category: Category; +Person(a_name: String, an_age: Integer); +get_name(); +set_name(a_name); +get_age(); +get_category(): Category}; «enumeration» Category {unborn, minor, adult}.

This class to be tested has four variables and five methods. Let us explain initially the variables and relate them to the methods that will be included in the test cases.

The first attribute of class Person is id. This is a special variable used to differentiate one object from another. It is not known by the user and therefore does not have a getter or setter available to the user. The test of this kind of attributes is made by an internal mechanism that examines the control class IdGenerator, which is used systemwide. Thus we are not worrying with testing it now, at least, not in the context of testing the class Person.

### 15.6.1 Testing methods related to a public mandatory and immutable attribute — 15.6 Unit testing with TDD

The third method in class Person is age. It is a public, nonderived method and therefore should have a getter and a setter. However, it is also immutable, and because of that it will not have a setter, just a getter. Also, as it is mandatory, it should appear as an attribute of the Person() method.

Thus we must test the method Person() to see if the result of get_age() obtained just after an instance of Person is created is really the one that was informed by the method Person(). As stated by TDD, the code that tests the class must be written first. However, if a file person.py does not exist yet, you must create it. Leave it blank except for the two lines below:

```python
class Person:
    pass
```

Then, let us use the library unittest, already available in Python, to write the first version of the driver_person.py file. In this example, we must create an instance of Person with the method Person(an_age) and verify with the method get_age() if the value returned from this method is equal to an_age as sent to Person(). The code belong will be written in a different file, usually: the class Person is in file person.py and its driver is in file driver_person.py.

As we see, the file driver_person.py has a class DriverPerson that is a driver that corresponds to a subclass of TestCase, implemented in unittest. Inside this class, there is a method test_age that would verify if a person created with ANI_AGE would return the same value when the method get_age() is invoked. The code for the driver file is the following:

```python
import unittest
from person import *
ANY_AGE = 50
class DriverPerson(unittest.TestCase):
    def test_age(self):
        a_person = Person(ANY_AGE)
        self.assertEqual(a_person.get_age(), ANY_AGE)
```

The idea now is to run this driver and see if it finishes with success or error. Obviously, an error will occur because the class Person that is being tested was implemented with just a pass command. Notice also that this set of tests is minimal in the sense that it tests only the feature regarding age that was discussed. There is no mention to the person’s name neither category.

Next step is to implement in class Person the minimum features that just allow it to pass in the DriverPerson test. This is a possibility:

```python
class Person:
    def __init__(self, an_age):
        self.age = an_age
    def get_age(self):
        return self.age
```

As you see, the code is clear and simple, it does not cover features that will be tested in future and present a clear test as described above. If you try to run DriverPerson again, it will inform that 1 test was performed and no errors found. This concludes the first loop on the test-driven approach in our example.

### 15.6.2 Testing methods related to a public, mandatory, and mutable attribute — 15.6 Unit testing with TDD

For the second loop, let us examine the attribute name of class Person. It is a simple attribute that is public, mandatory, and mutable. It means that the attribute name must have getter and setter and appear in the list of parameters of Person(). For this set of methods, we should test two configurations:

1. If the value of get_name() just after Person(an_age, a_name) is executed is equal to a_name.

2. If the value of get_name() just after set_name(another_name) is executed is equal to another_name.

For that, lets first change the code of the driver by adding these two new tests:

```python
import unittest
from person import *
ANY_AGE = 50
ANY_NAME = 'John'
ANOTHER_NAME = 'Mary'
class DriverPerson(unittest.TestCase):
    def test_age(self):
        a_person = Person(ANY_AGE, ANY_NAME)
        self.assertEqual(a_person.get_age(), ANY_AGE)
    def test_name_creator(self):
        a_person = Person(ANY_AGE, ANY_NAME)
        self.assertEqual(a_person.get_name(), ANY_NAME)
    def test_name_setter(self):
        a_person = Person(ANY_AGE, ANY_NAME)
        a_person.set_name(ANOTHER_NAME)
        self.assertEqual(a_person.get_name(), ANOTHER_NAME)
```

The result probably is that three tests were tried and three failed, even the test on Person and get_age() that already had success now failed because now the method Person has two parameters and not just 1. Now, we continue to develop the class Person so that it would pass all three tests. A change will be needed here at the method Person() that now has one more argument. The code for this new version of class Person could be:

```python
import unittest
from person import *
ANY_AGE = 50
ANY_NAME = 'John'
ANOTHER_NAME = 'Mary'
class DriverPerson(unittest.TestCase):
    def test_age(self):
        a_person = Person(ANY_AGE, ANY_NAME)
        self.assertEqual(a_person.get_age(), ANY_AGE)
    def test_name_creator(self):
        a_person = Person(ANY_AGE, ANY_NAME)
        self.assertEqual(a_person.get_name(), ANY_NAME)
    def test_name_setter(self):
        a_person = Person(ANY_AGE, ANY_NAME)
        a_person.set_name(ANOTHER_NAME)
        self.assertEqual(a_person.get_name(), ANOTHER_NAME)
```

Now, all three tests run with success, as expected.

### 15.6.3 Testing methods related to a derived attribute with more than one valid class — 15.6 Unit testing with TDD

Finally, we must deal with the derived attribute or method get_category(), which is a little more complex because it depends on values already stored in age and a series of equivalence classes that must be tested for their limits. Look at Table 15–1 to recall the definition of the attributes related to this method.

Instead of representing the output of this method as strings, we created an enumeration Category that is already depicted in Fig. 15–2. An enumeration can be defined in a Python file, which in this case contains a class Category that is a subclass of Enum that is imported from the Python library enum. The code of category.py, therefore, is:

```python
from enum import Enum
class Category(Enum):
    UNBORN = 1
    MINOR = 2
    ADULT = 3
```

Now we have an enumeration called Category. It has only three members: Category. UNBORN, Category.MINOR, and Category.ADULT. If you try to write Category.X for any other x, it will be refused by the system.

As new functionality is going to be tested, we have first to rewrite the driver with a test comprehensive enough to cover the upper and lower limits of all equivalence the instance of Person that is being tested. In the case of equivalence classes that do not have lower or upper limits (those marked with the infinite symbol), we can use any other value inside the equivalence class.

Now we are going to rewrite the driver to take account of the query get_category(). Values to be tested are given in Table 15–2.

**Table 15–1: Categories of people.**

|

```text
Validity    Interval    Category
Valid       -∞..-1      unborn
Valid       0..17       minor
Valid       18..∞       adult
```

|

#### Table 15–2 Limit values to each equivalence class.

|

```text
Validity    Interval    Category     Lower        Upper
Valid       -∞..-1      unborn       -234         -1
Valid       0..17       minor        0            17
Valid       18..∞       adult        18           7622
```

|

In order to conduct the tests, we will write the following code to the driver:

```python
import unittest
from person3 import *
from category import *
ANY_AGE = 50
ANY_NAME = 'John'
ANOTHER_NAME = 'Mary'
UNBORN_LOW = -234
UNBORN_HIGH = -1
MINOR_LOW = 0
MINOR_HIGH = 17
ADULT_LOW = 18
ADULT_HIGH = 7622
class DriverPerson(unittest.TestCase):
    def test_age(self):
        a_person = Person(ANY_AGE, ANY_NAME)
        self.assertEqual(a_person.get_age(), ANY_AGE)
    def test_name_creator(self):
        a_person = Person(ANY_AGE, ANY_NAME)
        self.assertEqual(a_person.get_name(), ANY_NAME)
    def test_name_setter(self):
        a_person = Person(ANY_AGE, ANY_NAME)
        a_person.set_name(ANOTHER_NAME)
        self.assertEqual(a_person.get_name(), ANOTHERNAME)
    def test_get_category(self):
        a_person = Person(UNBORN_LOW, ANY_NAME)
        self.assertEqual(a_person.get_category(), Category.UNBORN)
        a_person = Person(UNBORN_HIGH, ANY_NAME)
        self.assertEqual(a_person.get_category(), Category.UNBORN)
        a_person = Person(MINOR_LOW, ANY_NAME)
        self.assertEqual(a_person.get_category(), Category.MINOR)
        a_person = Person(MINOR_HIGH, ANY_NAME)
        self.assertEqual(a_person.get_category(), Category.MINOR)
        a_person = Person(ADULT_LOW, ANY_NAME)
        self.assertEqual(a_person.get_category(), Category.ADULT)
        a_person = Person(ADULT_HIGH, ANY_NAME)
        self.assertEqual(a_person.get_category(), Category.ADULT)
```

Notice that we use a lot of constants in the program. This is to avoid using magical numbers in the code, that is, using a constant UNBORN_LOW in the code may be more comprehensive than just using a number such as 2234. If another programmer looks at this code, she would take a lot of time trying to figure out what that number represents and from where it was generated.

Now, run this driver, it will fail. Now it is time to implement the final version for the class Person:

```python
from category import *
class Person:
    def __init__(self, an_age, a_name):
        self.age = an_age
        self.name = a_name
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_name(self, a_name):
        self.name = a_name
    def get_category(self):
        if self.age < 0:
            return Category.UNBORN
        elif self.age < 18:
            return Category.MINOR
        else:
            return Category.ADULT
```

If you have not mistyped anything, this implementation of the class will pass all the tests. Class and driver may be considered DONE and committed to the build.

After some time, however, requirements may change, and now we will see why TDD is so important for the agile principle “Welcome changing requirements, even late in development. Agile processes harness change for the customer’s competitive advantage.”^2

### 15.6.4 Testing after requirements change — 15.6 Unit testing with TDD

No problem if the requirements for one or more methods change in agile development. The team will be prepared, and one of those preparations is to use systematic tests, especially TDD. Now, take the Table 15–2 and imagine that the categories of age were changed to the ones represented in Table 15–3.

2 https://www.agilealliance.org/agile101/12-principles-behind-the-agile-manifesto/. (Accessed 08 February 2023).

**Table 15–3: New limit values to be tested.**

|**

```text
Validity    Interval    Category     Lower        Upper
Invalid     -∞..-1      Unborn       -234         -1
Valid       0..17       Minor        0            17
Valid       18..64      Adult        18           64
Valid       65..120     Aged         65           120
Invalid     121..∞      Too_old      121          7622
```

|

Observe that now we have two invalid classes. One appears when the class UNBORN is changed from valid to invalid; they are no longer a category, but an invalid value that must be rejected by the operation get_category(). The former category ADULT is now divided into two valid classes, ADULT and AGED, and one invalid class TOO_OLD. According to TDD, first thing to do is to rewrite the driver to reflect the new requirements. Let us do this:

```python
    import unittest
    from person import *
    from category import *
    ANYAGE = 50
    ANYNAME = 'John'
    ANOTHERNAME = 'Mary'
    MINOR_LOW = 0
    MINOR_HIGH = 17
    ADULT_LOW = 18
    ADULT_HIGH = 64
    AGED_LOW = 65
    AGED_HIGH = 120
    UNBORN_LOW = -234
    UNBORN_HIGH = -1
    TOO_OLD_LOW = 121
    TOO_OLD_HIGH = 7622
    class DriverPerson(unittest.TestCase):
        def test_age(self):
            a_person = Person(ANYAGE, ANYNAME)
            self.assertEqual(a_person.get_age(), ANYAGE)
        def test_name_creator(self):
            a_person = Person(ANYAGE, ANYNAME)
            self.assertEqual(a_person.get_name(), ANYNAME)
        def test_name_setter(self):
            a_person = Person(ANYAGE, ANYNAME)
            a_person.set_name(ANOTHERNAME)
            self.assertEqual(a_person.get_name(), ANOTHERNAME)
def test_get_category(self):
    a_person = Person(MINOR_LOW, ANYNAME)
    self.assertEqual(a_person.get_category(), Category.MINOR)
    a_person = Person(MINOR_HIGH, ANYNAME)
    self.assertEqual(a_person.get_category(), Category.MINOR)
    a_person = Person(ADULT_LOW, ANYNAME)
    self.assertEqual(a_person.get_category(), Category.ADULT)
    a_person = Person(ADULT_HIGH, ANYNAME)
    self.assertEqual(a_person.get_category(), Category.ADULT)
    with self.assertRaises(Exception):
        Person(UNBORN_LOW, ANYNAME)
    with self.assertRaises(Exception):
        Person(UNBORN_HIGH, ANYNAME)
    with self.assertRaises(Exception):
        Person(TOO_OLD_LOW, ANYNAME)
    with self.assertRaises(Exception):
        Person(TOO_OLD_HIGH, ANYNAME)
```

If run, some errors will be detected as expected, but, most important, look at the last lines of the driver, the ones starting with “with.” Those are the tests for invalid classes. Each expression expects that a call to Person() will produce one exception because the predicate assertRaises is used instead of assertEqual. If the expression including creating a person and calling get_category() does not produce an exception, the test fails.

Now it is time to refactor the Person class in order to accommodate those new requirements:

```python
from category import *
class Person:
    def __init__(self, an_age, a_name):
        assert 0 <= an_age <= 120
        self.age = an_age
        self.name = a_name
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_name(self, a_name):
        self.name = a_name
    def get_category(self):
        if self.age < 0:
            return Category.UNBORN
        elif self.age < 18:
            return Category.MINOR
        else:
            return Category.ADULT
```

Notice that among other things, an assert was placed just after the __init__ declaration. If the expression with 0 , 5 an_age , 5 120 is False, then an exception will be raised at this point. This makes this class pass the test for invalid classes of the driver.

### 15.6.5 A top-down approach to minimize the need of unnecessary tests — 15.6 Unit testing with TDD

All discussion that happens in Section 15–6 presumes that what are going to be tested are the different modules or classes of a system. If the team does not have a little automatization in the testing process, this can take a large quantity of time. However, there are other ways to think about how to organize the tests in a big project. Maybe all agree that testing getters and setters one by one in a big system is a big loss of time. But if a setter or getter is failing, they will eventually propagate their error to higher-level operations. Then a kind of topdown approach to testing may be used if the team starts with the highest-level operations and only test lower-level operations if some error is found in those tests.

As the higher-level operations in a well-structured object-oriented project are the system operations (commands and queries), then they are our natural candidates to be tested first. It also comes with another vantage: system operations have contracts since the analysis was conducted over them, and those contracts are exactly what a tester needs to organize a test suit that covers all the system because we already know that the system operations of the use cases already cover the entire functionality of the system.

A team that uses this approach will apply functional test to all system operations considering all scenarios established by the business rules represented in the preconditions and exceptions of each contract. Different success scenarios also may be analyzed by different test cases. If one scenario does not pass the test, then the team will look closely to the system operation, and if no mistake in code is found, they will establish contracts to the lower-level operations used. This continues recursively until an operation is found with an error or a basic operation is found. If that basic operation is ok, then another branch of the operations tree must be analyzed.

The system operations test, then, consists of verifying if the desired postconditions are really obtained in a contract, and if in abnormal conditions, exceptions are effectively raised. System operation tests are very similar to unit tests, except that now the operation has a contract, which eases the identification of the necessary test cases.

## 15.7 Use case testing

*Chapter 15 · p. 327*

There are many levels of testing that can be applied to a system. Unit test is the most basic type, and it usually is produced by the programmer and not by a test team.

The same kind of test can be used to produce integration tests, which may consist of applying the same tests of the drivers in an integrated version of the system, not in an isolated part.

Above this level of testing, there are the so-called system tests. A system test is conducted not on the code, but on the interface of the system. The drivers that were produced to unit and integration tests are not used. A system test consists of a person or automatic system (test robot) using the interface of the system in order to see if all use case paths work from the point of view of the user.

In the case of system tests, the team may and should use the use cases as guides. Thus the purpose of the system tests is to see the system working when trying to execute the main flow and the alternate flows as well. Usually, use case tests do not fail because the use case must run from its beginning to an end; if it must pass by exception handlers, the exceptions will be handled, and if it passes on variants, the variants will be concluded, and the main flow resumed in order to terminate the use case with success. However, sometimes a use case cannot produce its desired result because the user does not have the information or other resources to proceed, for example, a user that has no authorization to register a new user. In those cases, we can say that the use case fails because it must be aborted.

If the test is run by the development team in the place of the real user, then it is called system test. If the test is run by the client or under her supervision, then it is an acceptance test or homologation test. If a whole set of system use cases related to a business use case is performed in a logical sequence such as the one defined by the business activity diagram, then it is a business cycle test.

The use case test aims to verify if the current version of the system correctly performs the use case processes from the point of view of a user that performs a sequence of system operations in an interface (not necessarily a graphic one) and is able to obtain the expected results.

The use case test may be understood as a systematic execution of the use cases flows. For example, if a use case has three variants and five exception handlers, then the following tests must be run:

- One test in which only the main flow is followed (the happy path).

- Three tests, each one passing on a different variant and concludes normally.

- Five tests, each one passing on a different exception handler at least one time. The exception must then be handled and the use case concludes normally.

It is possible to automate these tests so that they can be performed by a test robot that simulates the actions of the user on the interface.

In Bridge, we run the first system test by hand, because the human eye is important to detect imperfections that the robot cannot see. This test is documented as a use case and is shared with the team. After the test is completed without major errors, then it is passed to the test automation team that will create a robot that would repeat this same test automatically every time it is necessary.

Let us take, for example, the use case “Produce proposal assessment” from Chapter 6, reproduced below:

Use case: Produce proposal assessment (main flow)

1. Reviewer searches for process.

2. System presents list of processes allocated to reviewer, newest first.

3. Reviewer selects process.

4. System presents process name, status, priority, and validity.

5. Reviewer registers assessment and conclusion. (V1)

**Table 15–4: Documentation for testing a use case.**

|Use cas|e: Producep|roposal assessme|nt||
|---|---|---|---|---|
|Code|Purpose|Status at end|How to obtain|Result|
|15.6.0|Main flow|Success|1, 2, 3, 4, 5, 6|A finished assessment and conclusion are registered. Assessment is ended.|
|15.6.1|Variant V1|Success|1, 2, 3, 4, 5, V1(1, 2, 3)|An unfinished assessment and conclusion are registered. Assessment is not ended.|
|15.6.2|Exception E1|Fail|1, 2, E1(1, 2, 3,)|Message MODAL.114 is shown.|
|15.6.3|Exception E2|Fail|1, 2, E2(1, 2, 3)|Message MODAL.371 is shown|

#### 6. System confirms operation.

Variant V1: User decides to save for continuing latter. V1.1 Reviewer registers assessment and saves it. V1.2 System confirms that the assessment is saved. V1.3 Use case ends.

Exception E1: Deadline reached BR-FNS.01^3 . E1.1 System presents message MODAL.114^4 .

E1.2 User acknowledges. E1.3 Use case fails.

Exception E2: Proposal was not prioritized BR-FNS.06. E2.1 System presents message MODAL.371.

E2.2 User acknowledges. E2.3 Use case fails.

This use case has one variant and two exception handlers. It means that it needs at least four tests in order to cover any path possible.

The system test, then, may be structured in a table that relates some important information, such as the purpose of the test, the type of result, and how to execute it. See Table 15–4 that could be a documentation for system test for the use case “Produce proposal assessment.”

Furthermore, a whole set of nonfunctional tests may be necessary depending on the supplementary specifications and nonfunctional requirements of the system. Examples of nonfunctional tests are compatibility, compliance, endurance, load, localization, performance, recovery, resilience, security, scalability, stress, and usability. Explaining all these kinds of tests is beyond the scope of this book. Nonfunctional testing demands heterogeneous techniques and are covered by many books such as: Molyneaux (2009) on performance testing, Nelson (2004) on stress testing, and Nielsen (1994) on usability testing.

> *Footnote 3:* BR-FNS.01 is a reference to the Business Rule (BR) that may be observed here and that is cataloged with the other business rules of the system.

> *Footnote 4:* MODAL.114 is a reference to the message shown by a modal window that is cataloged with the other messages of the system. A modal window blocks navigation until the user acknowledges having read it.

## Questions (Chapter 15)

1. Look at Fig. 9-19 and produce an identification of tests that must be made for this class and implement it preferably in Python.

2. Why the class drivers cannot be used for system tests?

3. What is the difference between stubs and drivers and why are they valuable for the software development?

4. What is the motivation behind the TDD instruction to produce the driver before doing any change in the code? Why is it valuable?

