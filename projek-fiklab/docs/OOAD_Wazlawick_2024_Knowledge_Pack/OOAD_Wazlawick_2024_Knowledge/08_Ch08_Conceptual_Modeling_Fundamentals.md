<!-- Knowledge file: Chapter 8 — Conceptual modeling: fundamentals -->
> **About this file.** Chapter 8 of a cleaned, AI-ready edition of Wazlawick, R. S. (2024). Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-443-13739-6.  
> **Covers:** Conceptual model fundamentals: attributes (types, initial values, derived, enumerations, primitive types, «unique»), concepts, associations (roles, multiplicity, derived, aggregation/composition, n-ary).  
> **Use this file when:** building a domain/class diagram: choosing attributes, classes and associations correctly.  
> **Sections:** 8.1 Introduction to conceptual modeling (p. 119); 8.2 Attributes (p. 123); 8.3 Concepts (p. 130); 8.4 Associations (p. 131)  
> **Contains:** 24 figures transcribed as text, 10 code listings.

# Chapter 8: Conceptual modeling: fundamentals

*Source: Wazlawick, Object-Oriented Analysis and Design for Information Systems, 2nd ed. (Elsevier, 2024), starts p. 119*

Key topics in this chapter

- Attributes

- Concepts

- Associations

## 8.1 Introduction to conceptual modeling

*Chapter 8 · p. 119*

Domain analysis consists of discovering and modeling information that must be managed by the system. This means that the team should discover how the information must be structured and transformed. It starts early with the preliminary conceptual model and continues during the sprints, when that model is refined and completed with information obtained in the use cases and/or system sequence diagrams.

The team may analyze two aspects of information: static (also called structural), which is being introduced in this chapter, and functional, which will be introduced in Chapter 12. The static aspect of the information is therefore represented in the conceptual model and the functional aspect in the system operation contracts.

At this point, when the team is completing and refining the conceptual model, they are still looking the system as a black box. Information may enter and leave the system frontier, but the team is not worried about how it is processed internally. The dynamic model, consisting of the collaborations among objects, will be introduced in Chapter 13.

The conceptual model describes information that the system is going to manage. It is an artifact from the problem domain, not the solution domain. Therefore, the conceptual model should not be confused with the Design Class Diagram, which belongs to the software internal architecture.

The conceptual model should not also be confused with the data model, because the data model emphasizes stored data representation and organization, while the conceptual model aims at representing the comprehension of information by users and not its physical representation. Thus, a relational data model is just one of the possible physical representations of a more essential conceptual model.

An interesting way to comprehend the conceptual model is to imagine that the elements described by it correspond to information that initially exists only in the mind of the user, as represented in Fig. 8–1, and not in a physical store system.

A user sends information to the system and receives information back from the system through system events and returns, respectively. At this point, the system does not even 

121 need to be considered a computational system, because the information exists independently of computer support for storing and managing it. The goal of the analysis is to study the problem, not the solution yet.

**Figure 8–1: The conceptual model as a representation of the user knowledge.** *(p. 122)*

> **Diagram content (transcribed from the figure image):** The conceptual model as a representation of the user's knowledge: an Actor with a thought cloud containing the preliminary conceptual model of Fig 4–5 (Cancellation, Proposal, Municipal Manager, Federal Manager, Sending, Proposal Assessment, Funds Deallocation, Funds Allocation, Phase Completion Requisition, Phase Assessment, Publication with their multiplicities).

The system solution could even be designed without computer technology. It is possible to analyze a whole situation and then propose a manual solution to implement it, in which, for example, data are stored in paper sheets, and operations performed by clerks using pencil, eraser, and staplers.

Just like essential use cases, the conceptual model is technology-independent. It should contain only elements that belong to the domain of the problem, leaving to the design the elements of the solution, that is, all elements related to technology, such as interfaces, storage, and communication.

The conceptual model represents only the static aspect of the information. Therefore, in the conceptual model, references to operations or dynamic aspects of the system cannot exist. Although the conceptual model is represented by the UML class diagram, the team should not yet include any methods. They will be included by using a specific technique introduced later in the book.

When the UML class diagram is used for conceptual modeling, there are precisely three kinds of elements to use for representing information:

- Attributes: Simple alphanumeric or primitive information, such as numbers, texts, and dates. Examples of attributes in the SISMOB project are reviewer’s name, payment date, project title, and total cost of a work. An attribute is always connected to a more complex element: the concept.

- Concepts: The representation of the complex information that has coherent meaning in the domain. Concepts usually aggregate attributes and cannot be described merely as alphanumeric. Concepts also may be related to each other by associations. Examples of concepts in the SISMOB project are Proposal, Publication, Phase Assessment, and Municipal Manager (not to be confused with the actor “Municipal manager”).

- Associations: A kind of information that links different concepts. However, associations are more than mere links: they are information. In the SISMOB example, associations should exist between proposals and municipal managers, and between funds allocation and publication, for example.

These three elements are detailed in the next sections. It is practically impossible to explain one without mentioning the others, because the three are strongly intertwined.

## 8.2 Attributes

*Chapter 8 · p. 123*

Attributes are, in the conceptual model, the alphanumeric and primitive elements such as date, money, number, string, and interval.

Although most programming languages allow attributes to be defined as data structures such as lists, arrays, sets, and trees, it is not recommended that such structures could be used as attributes of a class. That would be an antipattern and would violate one of the most fundamental principles of object-oriented modeling, which is called high cohesion. Later, when discussing modeling patterns, this issue is revisited.

Complex concepts (classes) names should also not be used as attributes of other concepts (although, again, programming languages allow that). For example, a reviewer should not be an attribute of an assessment. If a relationship between reviewers and assessment should exist, then an association should be used instead, because reviewers and assessment are considered as complex concepts in the context of the SISMOB project.

### 8.2.1 Attribute types — 8.2 Attributes

Attributes may have a type, although this is not mandatory for the conceptual model. Fig. 8–2 show two versions of a class without and with attribute types.

Types in conceptual models have the same meaning they have in programming languages. In Fig. 8–2 (right), we have the classical types: Integer and String, and a primitive user-defined type: Date^1 .

1 Although for some programming languages, date may be also a primitive type.

**Figure 8–2: A class with untyped attributes (left) and typed attributes (right).** *(p. 124)*

> **Diagram content (transcribed from the figure image):** Class Assessment with attributes, first untyped (+number, +due_date, +date_delivered, +text, +confidential_remarks) then typed (+number: Integer, +due_date: Date, +date_delivered: Date, +text: String, +confidential_remarks: String).

When an attribute is defined by formation rules, such as date and phone, it may be represented as a primitive class, which are highly reusable and used in the diagram as a type, not a class. Primitive types are introduced below in the text.

An address is something special. Is it an attribute or a complex concept? Is it simply a string or a complex concept composed of number, street, ZIP code, city, etc.? This case, as many others, is decided by analyzing the information needs of the users. If addresses are used just to print envelopes and send snail mail, then they behave merely as strings, and may be represented as attributes with type String. However, if addresses are used to calculate distances and routes, or if they are used to group customers that live in the neighborhood, then they behave as complex concepts and should be modeled initially as a primitive type. Furthermore, if they have a structure of associations between them or other classes, then they could be modeled as complex concepts.

### 8.2.2 Initial values — 8.2 Attributes

An attribute may be declared with an initial value. That means that every time a new instance of the concept is created, that attribute will automatically receive a defined initial value, which can be changed later if necessary. Unless stated differently, all attributes of a class are null when the class is instantiated. There are two ways to avoid an instance to exist without filling those mandatory attributes: the first, is to declare the attribute with an initial value, and the second is to pass the initialization value as an argument for the method that creates instances of that specific class.

In the SISMOB system, an Assessment instance may be created, for example, with a due date corresponding to the number of days, which is a known constant or variable, plus the current date. Considering that both values could be obtained from a service class such as “Sismob,” the Assessment class could be represented like in Fig. 8–3. In that figure, it is also represented the number of the assessment being obtained as a system variable plus one and the text attributes initialized with the empty string (“”), which is different from null. In the case of this class, the only attribute that would be null when the class is instantiated is date_delivered.

The definition of an initial value for an attribute may also be created with the use of the Object Constraint Language (OCL) (Object Management Group, 2010).

**Figure 8–3: Attributes with initial value.** *(p. 125)*

> **Diagram content (transcribed from the figure image):** Assessment with initial values: +number: Integer = Sismob.last_assessment_number()+1; +due_date: Date = Sismob.today()+Sismob.assessment_term(); +date_delivered: Date; +text: String = ""; +confidential_remarks: String = "".

Every OCL expression should be declared in a context that corresponds to a class. Most OCL declarations also have a subcontext, consisting of a class property, that is, an attribute, association role, or even a method. When declaring the initial value for the attribute due_date in class Assessment, the context is Assessment and the subcontext is due_date. Thus, the OCL expression starts as:

```ocl
Context Assessment::due_date
```

Context Assessment::due_date

Optionally, the type of the attribute may be added:

```ocl
Context Assessment::due_date:Date
```

In order to indicate that the OCL expression is defining an initial value for an attribute, the expression “init”: is used, followed by the expression that produces the initial value for the attribute. As in the example, the initial value is a sum of two system variables, the complete expression may be defined as:

```ocl
Context Assessment::due_date:Date
    init: Sysmob.today()+Sismob.assessment_term()
```

The expression may also be simplified a bit by omitting the type of the attribute:

```ocl
Context Assessment::due_date
    init: Sysmob.today()+Sismob.assessment_term()
```

An attribute may have its initial value defined by more complex expressions too. However, the team must be aware that some values may not exist at the time that a class is instantiated and therefore, must be avoided as initial values.

### 8.2.3 Derived attributes — 8.2 Attributes

Derived attributes are understood as derived alphanumeric values only. If a “derived attribute” refers to objects or data structures containing objects, then they correspond to derived associations (Section 8.4.3). Derived attributes differ from normal attributes because they cannot be changed directly. In other words, they are read- only.

**Figure 8–4: A class with a derived attribute.** *(p. 126)*

> **Diagram content (transcribed from the figure image):** Class Item with derived attribute: +cost: Money; +price: Money; +/profit: Money = price-cost ("/" marks a derived attribute).

A derived attribute is calculated and must be defined by an expression. In the class diagram, a derived attribute may be represented by a slash (/) preceding the attribute name (and type), followed by “ 5 ” and the (OCL) expression that defines the value of the attribute. Fig. 8–4 shows an example in which profit is defined as the difference between price and cost.

Derived attributes may also be defined by natural language or formal language. In this book, the formal language OCL will be used every time an expression must be used. The expression in this example has a class as context (Item) and an attribute as sub context (profit). It is followed by the word “derive”: that indicates that the expression that follows it defines how the value of the derived attribute is calculated when it is read. The expression of the example of Fig. 8–4 defines profit by using the values of other two attributes of the same class: profit 5 price – cost. Thus, the OCL expression for defining this attribute is:

The OCL expressions init: and derive: need to be followed by a reference to an object. When this object is the instance which that corresponds to the context of the expression, it can be referred by the word “self,” which works much like the expression “this” in Java and “self” in other object-oriented languages.

The notation self.property allows to access the value of a property (attribute, association role, or method) belonging to the object. For example, in the context of the class Item, the expression self.cost denotes the value of the attribute cost of a given instance of Item. Thus, the OCL complete expression that defines the derived value for the attribute profit of class Item is:

```ocl
Context Item::profit:Money
        derive:
            self.price-self.cost
```

Context Item::profit:Money derive: self.price-self.cost

In OCL, it is possible to omit the expression self when the context is not ambiguous. In the example above, the expression could be simplified to:

```ocl

```ocl
Context Item::profit:Money
    derive:
          price-cost
```

```

**Figure 8–5: Enumeration.** *(p. 127)*

> **Diagram content (transcribed from the figure image):** Two packages: "General Enumerations" containing «enumeration» Weekday {Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday}; and an empty package "Conceptual Model".

In the Item context, price and cost may be nothing else but attributes of Item. Then, the word self may be omitted from the expression.

Derived attributes may not be directly updated. In the Item class of Fig. 8–4, only the attributes cost and price may be directly updated. The derived attribute profit is read- only: it is calculated as the result of its defining expression.^2

### 8.2.4 Enumerations — 8.2 Attributes

Enumerations are a midterm between concepts and attributes. They are basically strings and behave like that. But there is a predefined set of valid strings that constitutes the enumeration domain. For example, a weekday type enumeration, such as, Weekday, can only assume a value in a set of seven possibilities: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday. Thus, an attribute defined with that type, such as, dayOff:Weekday would only assume one out of those seven values, although it behaves just like an string.

Enumerations may appear in UML diagrams as stereotyped classes. It is suggested that enumerations that are domain-independent are not placed in the same diagram that contains the conceptual model, but in a special package intended to contain the enumerations, as shown in Fig. 8–5, because domain-independent enumerations (such as Weekday) are very reusable from application to application. Only domain-specific enumerations should be kept together with the other classes of the conceptual model so that people can see their meaning more easily.

> *Footnote 2:* At this point, some readers that are also programmers could be worried about performance issues with the code that will be used to implement derived attributes. As they are by definition “calculated,” it seems a waste of processing time to repeat those calculations if the original values of cost and price have not changed. However, the readers can stay calm because code optimization mechanisms are available for derived attributes. For example, the value calculated for a derived attribute may be kept in the cache and recalculated only when one of its components is changed. For example, profit must be recalculated only after the instance of Item changes the values of price or cost.

In UML, enumerations are defined as stereotyped classes. While they may have associations and attributes of their own, the team is not encouraged to use those features because they would turn the enumeration into a complex concept, and it would probably lose reusability. For example, consider the Weekday enumeration. It is simply a list of seven names. Suppose now that the team adds some attributes to the Weekday enumeration, such as working hours. Then, Monday to Friday would have working hours defined from 9 a.m. to 5 p.m., Saturday from 9 a.m. to noon, and Sunday may have no working hours at all. In this case, what is the difference between this enumeration and a complex concept as it also has attributes and possibly associations and even methods later? Instead of creating attributes or associations for an enumeration, it would be advisable to create a new complex concept that accommodates the enumeration as is and the other attributes that need to be added. In the example seen in Fig. 8–6, a new concept WorkingDay could be created with two attributes: day:Weekday (still a pure enumeration), and working_hours:TimeInterval (a normal attribute as explained above). Thus enumerations that are thought to incorporate extra functionalities should be maintained as they are and included in normal classes.

To remain reusable, an enumeration should not be able to access any other class through an association. The fact that WorkingDay in Fig. 8–6 has an attribute labeled with Weekday allows the normal class WorkingDay to access the enumeration Weekday but not vice versa. This keeps the enumeration uncoupled from the classes that use it, and therefore, it maintains the enumeration largely reusable.

Enumeration values in OCL may be represented by the enumeration name followed by “::” and the value name, for example, Weekday::Tuesday.

**Figure 8–6: An enumeration being used by a conceptual class.** *(p. 128)*

> **Diagram content (transcribed from the figure image):** Package "General Enumerations" with «enumeration» Weekday (Sunday…Saturday) and package "Conceptual Model" with class WorkingDay {+day: Weekday; +workingHours: TimeInterval} — an enumeration used as an attribute type.

**Figure 8–7: A primitive type.** *(p. 129)*

> **Diagram content (transcribed from the figure image):** «primitive» class ISBN with attribute «imm» +number: Integer and private operation -valid(): Boolean — a new primitive type with validation.

### 8.2.5 Primitive types — 8.2 Attributes

The team can and should define primitive types when they deal with attributes that have formation rules, as in the case of International Standard Book Number (ISBN). Primitive types may be defined as classes stereotyped with «primitive», as shown in Fig. 8–7.

The ISBN class, stereotyped in such a manner, behaves like a type that can be used to define attributes. It is not a complex concept like User, Proposal, etc. It has a value with public access (marked with “ 1 ”), and a validation predicate that is private (marked with “ 2 ”), meaning that it can be accessed only by methods inside the class itself. That predicate will be called to verify if the ISBN value is valid or not, while it is created from an Integer, considering its formation rule.^3 That predicate is, therefore, used in the constructor (the method that creates instances of the class) to guarantee that only valid ISBNs are created. Remember that conceptual classes do not have methods, but primitive types are not conceptual classes. They are user-defined, reusable low-level components.

Although the value of the primitive type has public access, it is normally accepted that it is immutable. That means that the value of the primitive type can be defined only at creation time and not updated later. This is to make it consistent with the idea of primitive data elements as constants, and not as objects. Objects may change their internal state, and constants usually do not.^4 The immutable stereotype that may be used in attributes is «imm», for short.

Some primitive types, such as Date and Money, are already available in some programming languages and database management systems. Other not-so-common types may be created by the team and reused extensively.

The primitive type formation rule must be defined syntactically, that is, by evaluating expressions that do not need to consult data stored by the system. If a formation rule depends on consulting attribute or association values, then it is not, probably, the case for a primitive type, but for a normal class. For example, the prime number formation rule may be checked without consulting objects and associations, but a registered city name may not be a primitive type, because to check if a string is a registered city name, it is necessary to query existing names of current cities stored in the system.

A primitive type usually is application-independent, that is, its meaning usually is independent from the system or project being developed, just as general enumerations. An ISBN has the same meaning and formation rule in any application domain that uses it.

> *Footnote 3:* The ISBN formation rule is explained in http://www.isbn.org/standards/home/isbn/us/isbnqa.asp.

> *Footnote 4:* Some languages such as Smalltalk allow constants to change their value in runtime, but this is not usually the case and is not recommended for most applications.

However, concepts such as User, Item, and Project may have different definitions in different applications and cannot usually be reused without some refactoring effort. Primitive types, on the other hand, are usually 100% reusable, without adjustments or modifications.

## 8.3 Concepts

*Chapter 8 · p. 130*

Concepts are more than alphanumeric values. They are also more than a bunch of attributes, because they carry meaning and may be associated to each other. Conceptual modeling may begin with concepts and associations only, as shown before, that is, attributes are not needed in the preliminary conceptual model. However, when concepts are examined in detail, they usually contain a coherent group of attributes.

### 8.3.1 Unique attributes — 8.3 Concepts

It is assumed that different instances of a concept are distinguishable from each other just by the fact that they were created independently. This is not the case with primitive types. Two dates, such as March 05, 2013 and March 05, 2013, are the same. But two customers named “John Doe” are not necessarily the same person. Some programming languages indeed use two comparison predicates, one to check if two objects are equal (they have the same values for their attributes) and another to check if they are identical (they share the same space in memory).

Different instances are therefore always distinguishable from each other, but additionally they may have attributes that are unique to them. Once an attribute has been stereotyped as «unique», two or more instances of the concept cannot have the same value for that attribute. One example of a unique attribute is the number of an assessment, which is unique for each assessment, while the other attributes may have identical values in different assessments (Fig. 8–8). Unique attributes usually are also immutable. It may be accepted as part of the definition of “unique,” or else, the attribute should use the two stereotypes.

Unique attributes must not be confused with database primary keys. Primary keys are used especially for database design to provide a unique identification for an instance. But «unique» and primary keys are not identical, because a concept may have only one primary key, but more than one unique attribute. Primary keys must also be hidden from the user, while unique attributes are known and used by the user. Unique attributes are closer to the idea of candidate keys in relational databases (Date, 1982).

**Figure 8–8: A class with a unique attribute.** *(p. 130)*

> **Diagram content (transcribed from the figure image):** Assessment with «unique» +number: Integer = Sismob.last_assessment()+1; +due_date: Date = Sismob.today+Sismob.assessment_term(); +date_delivered: Date; +text: String = ""; +confidential_remarks: String = "" («unique» marks an attribute whose value identifies the instance).

**Figure 8–9: A controller class.** *(p. 131)*

> **Diagram content (transcribed from the figure image):** The system controller class shown two ways: a class box «control» Sismob and the UML control icon (circle with arrow) labelled Sismob.

### 8.3.2 System control class — 8.3 Concepts

Usually, the conceptual model is expected to be a connected graph, that is, every concept has a path (a sequence of associations) connecting it to every other concept. When that is not the case, it is supposed that something is missing, that is, important associations or concepts have not been discovered yet.

Although some authors oppose it, a concept that represents the system as a whole (in our example Sismob) may be useful in the conceptual model if some precautions are taken. First of all, that concept should be declared as a Singleton;^5 and second, it should not have attributes, being just a control class. This class corresponds to the system controller or façade controller already mentioned before. It does not represent any data; it serves only as a point of reference to add associations to other classes, as seen in the following sections.

All concepts are associated directly or indirectly to the controller class in order to be accessible by the application.

The system controller class may be stereotyped with «control» or drawn using Jacobson’s (1994) icon, as shown in Fig. 8–9.

Later, the advantages of using the controller class are explained in detail. There are some situations that are nicely modeled as associations from the control class.

## 8.4 Associations

*Chapter 8 · p. 131*

When complex concepts are related, it is said that there is an association among them. Associations usually happen only between two concepts, but they can also be defined among three or more concepts. There may also be reflexive associations between instances of the same class. For example, the association that links parents to children is defined as a reflexive association from Person to Person.

When classes are associated, then their instances may be linked. For example, an instance of Assessment is linked to an instance of Reviewer and an instance of Proposal.

Associations may be tricky to identify in use case texts, especially because sometimes deciding if something is a concept or association may be fuzzy. For example, is an approval an association between a manager and a proposal? Or is it a concept? If it is considered a concept, which are its own associations and attributes?

5 A design pattern that states that a class with a single instance may be accessible globally.

Moreover, use case texts often mention operations that are not exactly static associations. Operations such as buying goods, or making a reservation, are dynamic transformations on data. They could produce instances of concepts to represent their existence. It is necessary to consider the difference between the (static) associations and (dynamic) operations:

- An association is a static relation that may exist between complex concepts, complementing the information about them in each moment (a snapshot of their state), or referring to new associative information (e.g., neighborhood or parent/children).

- An operation is the act of accessing and transforming existing information.

As a description of a dynamic process, a use case text is usually full of explicit references to operations; but associations usually must be inferred from the text, because they are implicit.

At a used car dealer, there are people who buy cars from other people. When someone buys a car, she is performing an operation. That operation changes the links between objects: one ownership link ceases to exist, while another is created in its place. But, as the transaction of buying has its own attributes, such as date, values, it would not be appropriate to represent an operation as an association, as shown in Fig. 8–10.

Why is that interpretation not adequate? The information about date of buying and value paid cannot be represented neither in the class Person nor in the class Car. A car may be sold many times and a person can buy many cars. Each time a car is sold to a person, a new piece of information is created, a transaction. In this specific case, a Sale (Fig. 8–11).

However, there are different ways people and cars may be associated besides ownership. A person may be passenger of a car, or its driver, or the association may represent merely that someone likes a given car. To eliminate such ambiguities, it is convenient in many cases to use a role name on one or both association ends to indicate which role a class plays.

**Figure 8–10: A operation unduly labeling an association.** *(p. 132)*

> **Diagram content (transcribed from the figure image):** AVOID (note: "If the transaction has its own attributes, do not represent it as an association"): Person —buy— Car, with the unanswered question "date? value?".

**Figure 8–11: A transaction being represented by a class.** *(p. 132)*

> **Diagram content (transcribed from the figure image):** Better: the transaction becomes a concept. Person —(role buyer / acquisitions)— Sale; Person —(role seller / sales)— Sale; Sale {+date: Date; +value: Money} — Car.

In Fig. 8–11, a sale has a buyer and a seller that are two (different) people. On the other way, a person has a set of acquisitions (of cars) and a set of sales. In the case of the two associations from Sale to Person, both ends (roles) are explicitly named.

In UML if a role is not explicitly named, then it may be referred by the name of the class at that end in lowercase. For example, still in Fig. 8–11, a sale has a “car” because the association does not explicitly label this end of the association. On the other hand, a car has a set of sales for the same motive.

If there are two or more (n) associations between the same classes, then at least n 2 1 of the roles in both ends must be explicitly labeled. Otherwise, the diagram is ambiguous and not in compliance to the UML definition.

Although UML allows an association to have a name, this feature is not recommended. Instead of giving a name to an association as in Fig. 8–12 (left), consider naming its two roles (right).

It may be easier and more useful to work with role names instead of association names. In practice, the team can ignore the fact that associations may have a name. Conceptual models can be perfectly clear with role names replacing association names. Role names are easier to give because they define navigation possibilities between concepts and are useful also for naming derived programming code elements such as the variables that would represent the association when the code is generated.

If by any means an association name is still needed, it is always possible to create it by composing the role names; the reverse is not true. For example, an association between a car and a person could be called fleet2owner, fleet_owner, or fleetXowner if it indeed needs to have a name (e.g., for reference purposes). In this case, use the names of the roles if they are explicit. Otherwise, use the name of the class in lower case. Also, the order in that the roles appear in the name does not matter: fleet2owner is the same as owner2fleet.

**Figure 8–12: Naming an association versus naming roles.** *(p. 133)*

> **Diagram content (transcribed from the figure image):** AVOID giving names to associations (Person —owns— Car) vs PREFER naming roles (Person role "owner" — Car role "fleet").

### 8.4.1 Role multiplicity — 8.4 Associations

In a conceptual model, it is fundamental to know how many elements a role accepts. For example, in the association between Person and Car with role name driver in Fig. 8–13, how many cars can someone drive? How many drivers can a car have?

The answer depends on a study of the nature of the problem and on the real meaning of the association, especially if it represents the present time or the past. For example, if the associations of Fig. 8–13 represent the present, then a car may have just one driver (one at a time). But if this association represents the past, then it is possible that a car had many drivers during different periods of time.

Thus, it is fundamental that the team decides clearly what the association means before deciding on its role multiplicity. They should remember that associations are static constraints; they represent links that may exist between the instances of the associated classes since the instant of their creation. Therefore, depending on the meaning of the association, it may have different role multiplicities.

There are, basically, two decisions to be made about the multiplicity of an association role:

1. Is the role mandatory or not? For example, should a person have at least one car? Should a car have at least one driver or owner?

2. Does the number of instances that may be linked through the role have a defined conceptual bound? For example, is there a maximum number or minimum number of cars that a person may drive or own?

The answers to these questions may be tricky. Regarding the first decision, for example, returning to the SISMOB project, it is expected that each proposal must have at least one assessment. But that does not qualify the assessment role for a proposal as mandatory, because a proposal can exist without an assessment for a period. Eventually, any proposal will hopefully be assessed, but not necessarily soon. Thus this role is not mandatory for the proposal.

The other tricky issue concerns the maximum number of elements that a role allows. Physically speaking, the maximum number of cars that a person may own is the number of cars that exist on planet Earth (the number is increasing, but it is defined at a given moment of time, even if it is hard to count). But as new cars are built, they may be purchased. Thus although there is a physical limit for the ownership role, there is no conceptual or logical limit. Thus the role should be considered virtually without upper bound.

Similarly, a proposal may have any number of assessments, even if a customary number is 3. If the maximum number of assessments is a permanent requirement, then the role may be labeled with 0..3 (meaning zero up to three assessments per proposal), and it will be implemented by and array, probably. However, if this requirement is transient, then more flexibility is needed, and the role should be labeled with– (meaning zero or more assessments per proposal), and being implemented by a linked list, probably.

**Figure 8–13: Associations without explicit multiplicity.** *(p. 134)*

> **Diagram content (transcribed from the figure image):** Two associations between Person and Car with role names: driver (Person→Car) and owner/fleet.

Role multiplicity in UML is represented by an expression where:

- The asterisk “– * ” means “any quantity,” and indicates that there is no upper bound.

- The comma “,” means “or.”

- Two dots “..” means “up to.”

The following are examples of the usual multiplicity limits for conceptual models:

1—exactly one

- 0..1—zero or one

- * —zero or more

- 1..– * —one or more

- 2..5—two up to five

- 2,5—two or five

- 2,5..8—two or from five up to eight

The multiplicity limits that include zero represent roles that are optional for a concept. All the other limits are mandatory.

Fig. 8–14 shows an example where one person may have a fleet with an undetermined number of cars (optional), and a person may be a driver of one car at most (also optional). On the other hand, it shows that a car must have a single owner (mandatory) and that it may have a driver or not (optional).

According to many countries’ laws, a car may have more than one owner, or it may be owned by a corporation; in some situations, a car may also have no owner at all. The conceptual model (such as the one in Fig. 8–14) represents not necessarily a general truth, but the information needed for a given application. For some information systems, it could be mandatory that a car, in order to be registered, have a single owner and that this owner must be a person. In this case, the conceptual model should represent the specific and pragmatic information needs for that system.

### 8.4.2 Association direction — 8.4 Associations

An association in a conceptual model should be nondirectional in principle, that is, the navigability of the association should not yet be determined (Booch et al., 2007). This is because for analysis purposes, it is only necessary to know whether two concepts are associated or not; dynamic design will decide on navigability later.

**Figure 8–14: Associations with explicit multiplicity.** *(p. 135)*

> **Diagram content (transcribed from the figure image):** Same with multiplicities: Person 0..1 driver — 0..1 Car; Person 1 owner — * fleet Car.

However, some exceptions may exist. For example, a derived association is necessarily unidirectional, and the same happens to associations coming from the façade controller, as seen below.

### 8.4.3 Derived association — 8.4 Associations

Just as useful as derived attributes are derived associations, that is, associations that instead of being represented physically are calculated from available information. For example, suppose it is often necessary to know which proposals a given municipality has already sent in the SISMOB system. Considering that proposals are linked to municipal managers and the municipality is associated to this manager, then municipalities and proposals would not have a direct association, as seen in Fig. 8–15.

If proposals are not linked directly to the municipality in the conceptual model, referring to that information could be a bit more complicated than expected.

Fig. 8–16 shows a tentative for resolving this issue, but there is a need to guarantee that every time a manager adds a link to a proposal, the same happens to the municipality. If this is not done, the model would represent inconsistent information. Thus it would require some checking mechanism (e.g., allowing only assessments that were issued to be associated also to the municipality).

Fig. 8–17 shows an example of how a conceptual model for SISMOB could relate proposals to municipalities using a derived association “/proposals.” In this case, the association is unidirectional and only navigable from Municipality to Proposal. That means that a municipality may consult its own proposals directly (without using “Municipal Manager”) but that a proposal not necessarily have direct access to its Municipality. If this is necessary, then a second derived association from Proposal to Municipality should be included.

The multiplicity of the destiny role of the derived association in Fig. 8–17 is multiple (– ) because by navigating on the normal associations, it can be seen that a municipality may have submitted zero or more proposals. On the other direction, despite the derived association being not navigable from Proposal to Municipality, a constrained role may be indicated because one Proposal has just one Manager and one Manager has just one Municipality. Thus the origin of the derived association in this case has multiplicity “1.”

**Figure 8–15: Proposal and Municipality only have indirect association.** *(p. 136)*

> **Diagram content (transcribed from the figure image):** Municipality 1 — * Municipal Manager 1 — * Proposal.

**Figure 8–16: Redundant associations.** *(p. 136)*

> **Diagram content (transcribed from the figure image):** AVOID (note: "AVOID using redundant associations for obtaining information that can be inferred"): Municipality 1 — * Municipal Manager 1 — * Proposal plus a redundant direct association Municipality 1 — * Proposal.

**Figure 8–17: A derived association.** *(p. 137)*

> **Diagram content (transcribed from the figure image):** BETTER (note: "use a derived association in this case"): Municipality 1 — * Municipal Manager 1 — * Proposal plus a derived, one-way association Municipality → * /proposals (navigable only toward Proposal; marked "/").

Usually, the multiplicity of a derived association is defined by the product of the multiplicities of the roles that must be navigated to reach the target concept. The following rules may be used to determine that multiplicity:

- The lower bound of the derived multiplicity is the product of the lower bounds of the roles in the navigation path.

- The upper bound of the derived multiplicity is the product of the upper bounds of the roles in the navigation path.

For example, if the multiplicities found in the path are 1.0.5, 2..– , and 1, then the derived multiplicity is 2..– , because the lower bounds are 1, 2, and 1, and 1 3 2 3 1 5 2. As the upper bounds are 5, undetermined (– ), and 1, we have 5 3 undetermined 3 1 5 undetermined.

However, if filters are applied to the definition of the derived association, the resulting multiplicity may be different. For example, if the derived association is defined so that it links a municipality to the last proposal it has send, then the derived multiplicity should be 1, and not– .

As opposed to normal associations that allow links between individual objects to be added and removed, a derived association may only be consulted (just like derived attributes, which are read-only).

A derived association may be defined by an OCL expression as well. The example of Fig. 8–17 may be defined as:

```ocl
Context Municipality::proposals
    derive:
          self.municipal_manager.proposal
```

The following observations can be made about this OCL expression:

- The context is the class at the origin of the derived association (Municipality). The subcontext is the role name of the derived association (proposals).

- The expression “derive”: is used just like with derived attributes.

**Figure 8–18: Another derived association that works like a filter.** *(p. 138)*

> **Diagram content (transcribed from the figure image):** Two derived associations from Municipality: /proposals (*) and /recent_proposals (*) to Proposal {+date: Date}; recent_proposals is a derived association with a filter (e.g., by date).

- What determines if the expression is defining a derived attribute or association is the context and the type of information that is returned by the expression. Derived attributes are defined by expressions that return an alphanumeric, enumeration, or primitive type, while derived associations are defined by expressions that return an object or a collection of objects, recursively.

In object-oriented programming languages, usually the “.” notation can be used only over a single object. OCL, however, allows it to be used over collections of objects.^6 If x is a collection, then the meaning of x.y is the collection of y that can be obtained as properties of x. For example, if the context is Municipality, then self.municipal_manager denotes the set of municipal managers associated with that municipality. Moreover, self.municipal_manager. proposal is the set of all proposals linked to the managers of a given municipality.

### 8.4.4 Derived association with filter — 8.4 Associations

A derived association may also be used to define a subset of objects from a set of linked objects by the application of a filter. For example, imagine that we want to have the information on the proposals sent by the municipality in the last 6 months only. This is a very dynamic derived association because its members may change as time passes or actions are done.

Let us complete our example by adding the attribute date to the class Proposal (Fig. 8–18). In this case, we could define another derived association that associates municipalities only with projects sent up to 6 months from now. Let us call this new association role recent_proposals.

It cannot be seen in the diagram, but the derived association in this case would have the following definition:

```ocl
Context:Municipality::recent_proposals:Set<Proposal>
    derive:
        self.municipal_manager.proposal->select(:a_proposal|
            a_proposal.date+Sismob.Date(6,0,0)>=Sismob.today()
        )
```

()

)

The OCL expression for this derived association has as the context the Municipality class, because it is at the origin of the association. The expression that defines the derived association must denote the set of proposals with date not older than 6 months. This can be obtained by the condition a_proposal.date 1 Sismob.Date(6,0,0) . 5 Sismob.today()

> *Footnote 6:* In fact, in OCL, even a single object is considered a collection with a single element. This is equivalent to the natural notion of a set, but not to the mathematical notion of set, because in set theory, a set with one element is not the element. In OCL a set with one element and the element are the same thing.

In this expression, the operation Date in class Sismob creates an object of the primitive class Date with 6 months, 0 days, and 0 years, following the order of the arguments.

The OCL expression to obtain a subset of elements that satisfy a given Boolean expression like this is select. The Boolean expression is placed inside parentheses after the select command. The Boolean expression usually starts with an iteration variable that in the case of the example is:a_proposal|.

The arrow notation “- . ” is used before select instead of the dot (“.”) notation because the select function is applied over the structure of the set, not over its elements.^7

OCL also allows the iteration variable to be omitted if the context of the expression is not ambiguous. Thus, we can simplify the expression by omitting the “self” expression as well as the explicit iteration variable:

```ocl
Context:Municipality::recent_proposals:Set of Proposal
    derive:
        municipal_manager.proposal->select(
            date+Sismob.Date(6,0,0)>=Sismob.today()
        )
```

()

)

Observe that inside the parentheses after select the context is potentially ambiguous. There, the property date could refer both to a Municipality (broader context) and to a Proposal (narrower context). What allows us to eliminate the ambiguity is the fact that the property date does not exist in the class Municipality. If it existed in both classes, then the nonabbreviated notation should be used to eliminate the ambiguous expression.

### 8.4.5 Aggregation and composition — 8.4 Associations

Some associations may be considered stronger than others in the sense that they define one kind of object that is composed of others. A house, for example, is composed of rooms, a book of chapters, an undergraduate career of courses, etc.

If the association is exclusive, in the sense that an object may not be part of another object at the same time, then it is considered a strong part-whole association, which is called a composite aggregation,^8 and it is drawn with a black diamond on the role that represents the whole (Fig. 8–19).

7 In the case of a set of people p, if someone wants to get the set of all ages, she could write p.age. However, the size of the set is not a property of the people; it is a property of the set structure. Thus, to obtain the size of the set the expression p- . size() should be used. If it was written as p.size, then it would be representing the set of the sizes of each person (whether such information exists), not the size of the set.

8 “An association may represent a composite aggregation (i.e., a whole/part relationship). Only binary associations can be aggregations. Composite aggregation is a strong form of aggregation that requires a part instance be included in at most one composite at a time. If a composite is deleted, all of its parts are normally deleted with it. Note that a part can (where allowed) be removed from a composite before the composite is deleted, and thus not be deleted as part of the composite. Compositions may be linked in a directed acyclic graph with transitive deletion characteristics; that is, deleting an element in one part of the graph will also result in the deletion of all elements of the sub graph below that element” (Object Management Group, 2011).

**Figure 8–19: Example of composition.** *(p. 140)*

> **Diagram content (transcribed from the figure image):** Composition: Car (whole) with filled diamonds to Engine (0..1 — 0..1), Seat (0..1 — *), Wheel (0..1 — *).

**Figure 8–20: A shared aggregation.** *(p. 140)*

> **Diagram content (transcribed from the figure image):** Shared aggregation (hollow diamond): Career 1..* ◇— 1..* Course (a course can be part of several careers).

The multiplicity of the role that represents the composite (the side where the diamond is), in the case of a composite aggregation, should be 1 or 0..1, and nothing else, because composites do not share parts, even with objects of the same class.

In the example, it is considered that a car is made of engine, wheels, and seats. However, as each of those components may be removed from a car and keep existence, both the role from the car and from the components is optional (0..1 or– ).

Composite aggregation indicates exclusivity in the part-whole association. When this exclusivity is not mandatory (the part may be part of other aggregates), then a white diamond is used instead, and the association is called a shared aggregation (Fig. 8–20).

The white diamond indicates a shared aggregation where the part may belong to different wholes at the same time. In Fig. 8–20, a given Course may be part of one or more Career. This example shows a component that can be shared by many instances of the same class.

A different situation is when a component may be shared among instances of different classes. In Fig. 8–21, an Item must be part of an Order, but it could be part of a Sale.

**Figure 8–21: Shared aggregation of different classes.** *(p. 141)*

> **Diagram content (transcribed from the figure image):** Aggregations: Order 1 ◇— 1..* Item; Sale 0..1 ◇— 1..* Item.

Composite and shared aggregations are special associations and should be used with much parsimony, that is, they should be used only when the team is sure that it is the case that an object is really part of another and not just a normal association. Even the UML specification (Object Management Group, 2011) states that the precise semantics of a shared aggregation vary between application areas and modelers.

It is common to see aggregation and composition being abused in models when objects that are not part-whole related are linked by that kind of association. For example, a reviewer is not part of an assessment, if not for any other reason, but by the fact that a reviewer is a person and a text produced by a person does not become part of the person, neither the reverse.

Composite and shared aggregations should unite elements of the same nature: physical with physical, and abstract with abstract. If a Car is a physical thing, then its parts should be too. If a Career is an abstract thing, then its parts would also be abstract.

There are few real advantages in using aggregation in conceptual modeling. This is another reason to minimize or even abolish their use if the team still confuses the concepts. Among the advantages is that composite or shared aggregation parts usually have attributes and operations that are combined and derived in the whole. For example, the weight of a Car is derived as the weight of all its pieces, and if a Car is sold, all of its parts are sold too.

### 8.4.6 n-ary associations — 8.4 Associations

Most associations are binary, that is, most associations have only two roles. However, there are situations where associations with three or more roles are needed. In UML, these associations can be represented by using a diamond that connects all the roles of the association, as in Fig. 8–22.

The example in Fig. 8–22 was taken from a budget control application. Each project may be associated to multiple budget items and multiple financial years. Each financial year may have a number of budget items per project. Each budget item is associated to a financial year and a project. A ternary association (i.e., an association with three roles) represents this situation better than binary associations.

A ternary association corresponds to a table with a triple index. Although it could be represented by binary associations with the introduction of an intermediate class, as in Fig. 8–23, the meaning is different. If a ternary is used, there can be only one combination of BudgetItem, FinancialYear, and Project. In the example of Fig. 8–23, many occurrences of SpendingValue can exists with the same BudgetItem, FinancialYear, and Project.

**Figure 8–22: Example of tertiary association.** *(p. 142)*

> **Diagram content (transcribed from the figure image):** Ternary association (central diamond) among BudgetItem (*), FinancialYear (*), Project (*).

**Figure 8–23: An option to a ternary association but with a different meaning.** *(p. 142)*

> **Diagram content (transcribed from the figure image):** Ternary association replaced by a concept: SpendingValue linked to BudgetItem (1 — *), FinancialYear (1 — *) and Project (1 — *).

**Figure 8–24: Correction of Fig. 8–23.** *(p. 142)*

> **Diagram content (transcribed from the figure image):** BAD (note: "many combinations allowed are not possible in reality"): ternary association Author–Publisher–Book (all *). BETTER (note: "authors only relate to a publisher by means of their books"): Author 1..* — * Book * — 1 Publisher.

These cases are not frequent, but they may appear in a project. Before deciding to use a ternary or n-ary association, the team should verify if they are not confusing it with a situation where a combination of binary associations should be used instead. For example, the case shown in Fig. 8–24 (left) is not correctly modeled as a ternary association, because the relation between the author and the publisher happens only when the author publishes a book with a publisher. Then, the configuration of Fig. 8–24 (right) is more adequate to the eventual requirements. Only in a scenario where the same author could publish the same book using a different publisher and the publisher could publish the same book with a different author would there be a case for a ternary association. But that is not the case.

## Questions (Chapter 8)

1. Why should an attribute not be typed with a class name? Why should an attribute not be used to reference another class?

2. What is the difference between a normal association, an aggregation, and a composition? When to use each of them?

3. What is an Enumeration and how to use it in conceptual modeling?

4. List some examples of data types that could be defined as primitive and enumerations. The more the merrier.

5. What is the difference between initial valued and derived attributes?

This page intentionally left blank

