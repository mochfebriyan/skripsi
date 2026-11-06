<!-- Knowledge file: Chapter 9 — Conceptual modeling: data structures and organization -->
> **About this file.** Chapter 9 of a cleaned, AI-ready edition of Wazlawick, R. S. (2024). Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-443-13739-6.  
> **Covers:** Collections (set, bag, sequence, ordered set, map, partition, relation), organization of the conceptual model (generalization, association classes, roles vs subclasses), modal classes (states), invariants.  
> **Use this file when:** refining a class diagram: collections, qualifiers, inheritance vs roles, status attributes vs state classes, invariants.  
> **Sections:** 9.1 Collections (p. 143); 9.2 Organization of the conceptual model (p. 150); 9.3 Modal classes (p. 157); 9.4 Invariants (p. 163)  
> **Contains:** 27 figures transcribed as text, 4 code listings.

# Chapter 9: Conceptual modeling: data structures and organization

*Source: Wazlawick, Object-Oriented Analysis and Design for Information Systems, 2nd ed. (Elsevier, 2024), starts p. 143*

## Key topics in this chapter (Chapter 9)

- Collections: Set, Bag, Ordered Set, Sequence, Map, Partition, and Relation

- Organization of the Conceptual Model: Structural, Associative, and Temporal

- Invariants

## 9.1 Collections

*Chapter 9 · p. 143*

Simple collections of objects that do not have any particular meaning or structure should not, in principle, be represented as concepts, but as association roles. Any association role already represents a collection of objects of the associated class. Thus considering the example of Fig. 9–1 (up), fleet associates a set of cars to a person. The model presented in Fig. 9–1 (up) is, therefore, unnecessary and redundant, because the model shown in Fig. 9–1 (down) is equivalent and simpler.

Thus unless the fleet has its own attributes, associations, or methods (e.g., a person having multiple fleets located in different places), the correct form to represent a simple collection of objects is through an association role, not through a class.

Thus the team must be aware that if the collection has particular attributes or associations, then it must be represented as a concept (methods will be introduced latter). For example, an Order is initially understood as a set of items, but an Order also has attributes such as issue date, total value, and discount and associations such as the one with the customer, who may have multiple orders. If that is the case, the collection is not a simple role but a concept, as shown in Fig. 9–2.

Association roles may be thought as representing abstract data types (Liskov, 1974) in conceptual models. In design models, they would also represent concrete data types. Abstract data types are defined only by behavior, not by structure. They appear, for example, in the following:

- The set structure, in which elements do not repeat and have no defined position.

- The bag structure, in which elements may repeat but still do not have a defined position.

- The ordered set structure, in which elements do not repeat but have a defined position.

- The sequence structure, in which elements may repeat and have a defined position.

- The map structure, in which keys are associated to values.

- The partition structure, in which keys are associated to sets of values. 

145 

**Figure 9–1: How to represent a collection with no particular features.** *(p. 146)*

> **Diagram content (transcribed from the figure image):** AVOID (note: "redundant unless Fleet has its own attributes, associations, or methods"): Person 1 owner — 1 Fleet 1 — * Car. BETTER (note: "the collection fleet is already represented in the role of the association"): Person 1 owner — * fleet Car.

**Figure 9–2: A collection with particular features being represented as a concept.** *(p. 146)*

> **Diagram content (transcribed from the figure image):** Person 1 customer — * Order {+issue_date: Date; +total_value: Money; +discount: Money} 1 — * Item.

- The relation structure, in which sets of keys are associated to sets of values.

The concrete data types, on the other hand, are physical implementations for the abstract versions. For example, a list may be implemented in many forms, such as an array, binary tree, and linked list. In the case of concrete data types, besides behavior, there is a physical structure that defines them.

### 9.1.1 Set — 9.1 Collections

In UML, an association role, by default, is a set, that is, a structure where elements do not repeat and where there is no defined position for them. In Fig. 9–3, the fleet is an example of a set. On the other side of the association, the role owner also represents a set, but in this case, it should be always a set with no more and no less than one element, due to the multiplicity of the role (1).

If someone tries to link the same car to the same person a second time, nothing happens, because it already belongs to the set, and the set cannot repeat elements. However, if someone is replacing the owner by another person, it is possible, unless the role is immutable.

### 9.1.2 Ordered set — 9.1 Collections

Suppose a product that is not yet in stock has a list of people interested in buying it as soon as it is available. If it cannot be assured that the quantity of products received will fill all the orders, then the fairer way to attend to these customers is by establishing a line from the oldest reservation to the newest. This requires that the customers have a position in the line.

If the same customer cannot reserve the same product more than once, then it is still a structure with no elements repeated, but now with defined positions.

**Figure 9–3: A set.** *(p. 147)*

> **Diagram content (transcribed from the figure image):** Person 1 owner — * fleet Car (a role with multiplicity * is a set).

**Figure 9–4: An example of ordered set.** *(p. 147)*

> **Diagram content (transcribed from the figure image):** Product * reservations — customer * {ordered} Person — an ordered collection (list/sequence) of customers per product.

This leads to the ordered set structure. In the diagram, the role may be marked with the constraint {ordered} to indicate that it is a collection where elements do not repeat but have defined positions, as seen in Fig. 9–4.

The constraint {ordered} over an association role means that the elements linked on that role have position (first, second, third, . . ., last), but still cannot be repeated. Also, it does not mean that this collection is necessarily sorted.

### 9.1.3 Bag — 9.1 Collections

There are situations in which the position of the elements does not matter, but each element may appear more than once in the collection. That structure is called a bag.

For example, one may need to know how many people viewed the details of a product, and it may be important also to know how many times each one viewed it. It is not necessary to know who viewed it first, but the information on the number of views is necessary. That is a typical case for using a bag. Each time a person views the details of a product, a new link is added on the association role defined as a bag. The model is shown in Fig. 9–5.

### 9.1.4 Sequence — 9.1 Collections

The sequence allows elements to be repeated and also assigns a position to them. For example, imagine that people who buy a given value worth of product qualify for receiving a gift, but a limited quantity of gifts is available. Thus a list of people that qualify to receive the gift may be built, and the gifts will be distributed to the first members of the list as soon as gifts become available. If someone again buys more than the limit established to receive a gift, she can enter the list again. Thus in that structure, the position of an element is relevant, and each element may appear more than once: this corresponds to a sequence structure, as seen in Fig. 9–6. This is a typical situation in which using a controller in the conceptual model can help building better models. Otherwise, a class for controlling reservations would need to be created especially to contain this association.

**Figure 9–5: An example of bag.** *(p. 148)*

> **Diagram content (transcribed from the figure image):** Product * visualizations — viewers * {bag} Person — a bag (a person may appear several times among a product's viewers).

**Figure 9–6: An example of sequence.** *(p. 148)*

> **Diagram content (transcribed from the figure image):** Controller —(one-way, not navigable back, marked ×)→ * {sequence} qualified_for_gift Person — a sequence (ordered, repetitions allowed) held by the controller.

The multiplicity– * on the Controller side means that not all customers are qualified for a gift and that they may qualify more than once.

The sequence has two important special cases. When the first element to be removed is always the oldest in the sequence, as in the case of Fig. 9–6, then the structure is also a queue. UML does not define a constraint for queues, but a stereotype on the sequence constraint would do the job:– {sequence} «queue». When the first element to be removed is the newest in the sequence, then it behaves like a stack and may be stereotyped as such:– * {sequence} «stack». Queues and stacks that do not repeat elements may be defined respectively as– * {ordered} «queue» and– * {ordered} «stack». A general list may have elements removed and inserted at any position. Queues and stacks have elements inserted and removed only at predetermined positions, as explained above, although, in most cases, all their elements may be browsed.

A curiosity to be mentioned now is that in the real world, most collections are strict sets and not sequences, but even so, the most used programming structure is still the sequence or array, and not the set, which indicates a gap between reality and the data structures used in programming.

### 9.1.5 Map — 9.1 Collections

When a concept has a unique attribute, a map may be created from that attribute to the concept, in such a way that it is easier to identify and find specific instances of the concept. For example, as the ISBN is unique for a book, associations to Book may be qualified by the ISBN, meaning that instead of having a set of books, the origin class has access to a map that allows immediate identification of any book if its ISBN is known. Fig. 9–7 shows an example of qualified association.

The small rectangle at the left side of the association in Fig. 9–7 represents a qualifier for the class at the opposite side of the association (Book). Notice that instead of “– * ,” the role of the right side is now bounded by “0..1”; the association should now be read as follows: “for each possible ISBN there is no more than one book.”

**Figure 9–7: An example of qualified association.** *(p. 149)*

> **Diagram content (transcribed from the figure image):** Qualified association (map): Control with qualifier isbn:ISBN 1 — 0..1 Book {«unique» «imm» +isbn: ISBN; «imm» +title: String; «imm» +year: Integer; «imm» +pages: Natural} — finds a book by its ISBN.

Some valid ISBN values may not be associated to any book, because they were not registered in the system or because the ISBN, although valid, has simply not yet been assigned to any book; however, if one ISBN is taken by a book, no other book may share it. In practice, a qualified association is still an association “to many,” but the objects belonging to the role may be accessed by one of their attributes, instead of being searched inside a collection.

The role at the left side (the qualifier side) is marked with “1,” meaning that each book must have a single ISBN, neither less nor more. This must be necessarily true, because an ISBN is unique and not optional for the class Book, and therefore, it is mandatory and does not allow repetition. In this case, the ISBN is also immutable.

The qualifier is not only a method to access objects in an easier way. It is also a powerful modeling tool. For example, consider a situation where a person may own many phones, but only one of each kind. How do we represent this? The first naïve solution appears to be adding an attribute such as “type” in the class Phone. However, the type is not a property intrinsic to a phone; it is determined by how the person uses the phone. The phone can be a personal mobile, a professional mobile, a residence phone, etc. But it is not an attribute of the phone, it is a way a person relates to it. Then, a more elegant model for that situation is shown in Fig. 9–8.

In the case of Fig. 9–8, one person may have up to five phones, but just one of each kind. If more kinds are added to the enumeration later, then more phones may be associated to each person. If the role on the right side was 1 instead of 0..1, then one person should necessarily have five phones, each one of a different kind. That use of a qualified association with a mandatory role usually makes sense only when the qualifier is an enumeration or a finite set.

In the example of Fig. 9–7, the qualifier (ISBN) is an attribute of the qualified class, and in that case, it is called an internal qualifier. On the other hand, in Fig. 9–8, the qualifier (kind) is not an attribute of the qualified class, and it is called an external qualifier.

In Figs. 9–7 and 9–8, the multiplicity 1 or 0.1 on the right side of the figure means that the association is a mapping, that is, for each value of the key, there is at most one instance of the qualified class.

### 9.1.6 Partition — 9.1 Collections

What if instead of “1” or “0.1,” the multiplicity on the right side of the association was marked with “– * ”? In this case, the association would read as follows: “for each key there is a set of instances of the qualified class, not just one.”

**Figure 9–8: Modeling a situation with a qualified association.** *(p. 150)*

> **Diagram content (transcribed from the figure image):** Qualified association with an enumeration as qualifier: Person {+name: String} with qualifier kind:PhoneKind 1 — 0..1 Phone {+number: PhoneNumber}; «enumeration» PhoneKind {home, personal_mobile, professional_mobile, messages_only, night_phone}.

For example, books may be classified by genre. As many books may belong to the same genre, then the genre attribute may not be unique. But it is possible to define a partition on the set of books based on their genre, as shown in Fig. 9–9.

Fig. 9–9 states that for each particular value of genre, there is a set of books associated (with zero or more elements). The role multiplicity “1” on the left side indicates that every book has one genre.

### 9.1.7 Relation — 9.1 Collections

Now, imagine that a book may have more than one genre, for example, The Hitchhiker’s Guide to the Galaxy (Adams, 1979), which can be classified both as science fiction and humor. For representing the possibility of a book having more than one genre, it would be sufficient to change the multiplicity on the left side of the association to– * (if a genre is optional) or 1..– * (if at least one genre is mandatory). Additionally, the genre should be removed from the attributes of Book, because it is not a single value anymore, and the qualifier becomes external, because the genre key now associates to multiple books. Fig. 9–10 shows the resulting relation.

The relation of Fig. 9–10 states that a book may have one or more genres and a genre has a set of books associated with it. As a book may have more than one genre, then the qualifier should be necessarily external.

## 9.2 Organization of the conceptual model

*Chapter 9 · p. 150*

The elaboration of the conceptual model involves more than just putting concepts, attributes, and associations together. For the conceptual model to be a reliable and organized representation of real-world information, it is necessary to use some modeling techniques.

The main organizational techniques for concepts may be distinguished into three groups:

**Figure 9–9: Example of partition.** *(p. 151)*

> **Diagram content (transcribed from the figure image):** Partition: Controller with qualifier genre:BookGenre 1 — * Book {«unique» «imm» +isbn: ISBN; «imm» +genre: BookGenre}; «enumeration» BookGenre {mystery, romance, science_fiction, historical_romance, thriller, humor} — each genre maps to a set of books (book has exactly one genre).

**Figure 9–10: An example of relation.** *(p. 151)*

> **Diagram content (transcribed from the figure image):** Relation (multimap): Controller with qualifier genre:BookGenre 1..* — * Book {«unique» «imm» +isbn: ISBN}; same BookGenre enumeration — a book may be in several genres.

- Structural: Representing generalizations among concepts, for example, BankAccount generalizing SavingsAccount and CheckAccount.

- Associative: Representing associative roles that some concepts may play related to others, for example, Student and Professor being roles a Person may play related to a school.

- Temporal: Representing relations among different states of a concept, for example, an Order being in states AttendingPayment and Paid.

Novice analysts and sometimes even experienced ones tend to think that the only way to factorize information is by using inheritance or generalization. However, it is necessary to apply some judgment before deciding on using this or another technique. Inheritance may be used only when a concept effectively has two or more subtypes. Although UML allows an instance to change its class, only a few languages, such as Smalltalk (Goldberg and Robson, 1989), tried to implement such a feature, maybe because there are some unresolved inherent difficulties associated to the fact that one instance could change its internal structure on the fly.

Most object-oriented languages ignore this feature due to the problems it raises, and since it is usually unnecessary, because most behaviors that could be modeled by this feature also have alternate simpler representations. Thus for practical terms, it is usually the case that an instance may not change its class: it is born as a member of one class, and it will die a member of the same class.^1 As students may become professors, they do not qualify as subtypes of people.

Another counterexample is Worker and Customer being modeled as subclasses of Person. This is bad first because no one is born a worker or customer; a person becomes a worker or customer when associated to a company. More than that, the same person may be a customer or worker in more than one company. Using inheritance in this case would create conceptual problems that can produce duplicity in records and data inconsistency.

The following subsections present details on the three approaches to the organization of concepts.

### 9.2.1 Generalization, specialization, and inheritance — 9.2 Organization of the conceptual model

For years, inheritance was considered the most important feature of object-oriented languages. Languages such as Smalltalk, for example, were built over a single hierarchy of classes based on inheritance.

As time went by, this emphasis lost strength, because it was perceived that inheritance is not always the best idea for solving modeling problems. Today, inheritance is considered just one of the techniques that help to factorize information that otherwise would be repeated in classes.

Inheritance, in object-oriented systems, occurs when two classes relate through a special association called a generalization (or a specialization, depending on the direction you look). A class that generalizes another class is its superclass, and the specialized one is the subclass.

Generalization should be used every time there is a set of classes X1, . . ., Xn that have specific differences and common similarities, so that the similarities can be grouped in a superclass X (generalization of X1, . . ., Xn) and the differences maintained in X1, . . ., Xn.

Generalization/specialization has a semantic much different from the other associations of the conceptual model. It exists only between classes, not between instances as normal associations do. For example, if a class Reviewer is associated to the class Assessment by a normal association, then instances of Reviewer may be linked to instances of Assessment: the normal association allows those links to exist.

> *Footnote 1:* More specifically, an object is also an instance of all of its superclasses. The idea is that the set of superclasses should not change after the instance is created.

On the other hand, if a class BankAccount is a generalization of CheckAccount, then every instance of CheckAccount is also an instance of BankAccount (Fig. 9–11). There are not two instances to be linked, just one instance with the properties defined in both classes.

In the example, every instance of CheckAccount has three attributes: number, overdraft_limit, and overdraft_fee. However, not every instance of BankAccount is an instance of CheckAccount: the generalization is antisymmetric. An instance of BankAccount has only one attribute: number.

Thus one of the reasons to use inheritance is when there are some similar properties (attributes, associations, or methods) in different classes, which may be factorized in an abstract construct such as a superclass.

If the superclass may have its own instances, then it is a normal class. However, most of the time superclasses are defined not to allow direct instances: only their subclasses may have instances. In this case, the superclasses are considered abstract classes. Abstract superclasses are represented in UML by a class with its name written in italic, or, more visibly, with the constraint {abstract} (Fig. 9–12).

In Fig. 9–12, the BankAccount class is abstract and therefore cannot have direct instances; only its subclasses may have instances. Instances of CheckAccount have number, overdraft_limit, and overdraft_fee as attributes; instances of SavingsAccount have number and interest_rate as attributes. Both subclasses also inherit the association to the class Person labeled as customer, and all instances of both classes must, therefore, be linked to an instance of Person.

**Figure 9–11: An example of generalization/specialization.** *(p. 153)*

> **Diagram content (transcribed from the figure image):** Generalization: BankAccount {«imm» «unique» +number: AccountNumber} ← CheckAccount {+over_draft_limit: Money; +over_draft_fee: Percentage}.

**Figure 9–12: An example of abstract class.** *(p. 153)*

> **Diagram content (transcribed from the figure image):** Abstract superclass BankAccount (italic) {«imm» «unique» +number: AccountNumber} with subclasses CheckAccount {+over_draft_limit: Money; +over_draft_fee: Percentage} and SavingsAccount {+interest_rate: Percentage}; BankAccount * — 1 customer Person {«imm» +name: String; «imm» «unique» +id: ID}.

**Figure 9–13: A case where a superclass is not necessary.** *(p. 154)*

> **Diagram content (transcribed from the figure image):** AVOID ("creating a class that generalizes nothing"): Thing as superclass of Book {«imm» «unique» +isbn: ISBN; «imm» +title, +author: String; «imm» +year: String; «imm» +page_count: Natural} and Car {+license: License; +model: CarModel; +color: Color} — they share no attributes.

Generalization in not advisable when the superclass has no properties, that is, no attributes, associations, or methods of its own (Fig. 9–13). In this example, CarModel and Color are enumerations.

Generalization should also not be used when subclasses do not have properties (attributes, associations, or methods^2 ) that differentiate them from each other as in Fig. 9–14. One exception to this rule occurs when the superclass is abstract; in this case one, and just one, of its subclasses may not have properties of its own.

When subclasses do not have any properties, the ideal solution is to use a single attribute, possibly typed with an enumeration, to differentiate instance groups of objects (Fig. 9–15). In the example, we have considered that in some countries, name and gender may be changed legally. Thus we kept from considering those attributes immutable. Also, using an enumeration as gender, it is easier to add more genders if the requirements demand that; it should be only an update operation over an enumeration class. If subclasses were used, code should be written and compiled.

Besides these rules, before deciding on the use of inheritance, it is advisable to verify if the generalization really represents a structural classification of the elements and not an associative or temporal organization, as seen in the following sections.

### 9.2.2 Association classes — 9.2 Organization of the conceptual model

One issue frequently misunderstood in conceptual modeling is related to the definition of generalization among classes that are not really structural subtypes, but roles. For example, a

2 Methods are only considered when design classes are being modeled. Remember that conceptual classes do not have methods.

**Figure 9–14: A case where subclasses are not necessary.** *(p. 155)*

> **Diagram content (transcribed from the figure image):** AVOID ("creating subclasses that specialize nothing"): Person {«imm» «unique» +id: ID; +name: String; +address: String} with empty subclasses Man and Woman.

**Figure 9–15: A better option for the situation of Fig. 9–14.** *(p. 155)*

> **Diagram content (transcribed from the figure image):** Better alternative: Person {«imm» «unique» +id: ID; +name; +address; +gender: Gender} with «enumeration» Gender {male, female}.

store may have two “types” of people: customers and workers. After discovering that both have a name, address, phone, etc., an analyst could assume that they are two concepts that should be generalized as Person. But that apparently simple solution (Fig. 9–16) generates a complicated problem because they are not different types of people, but different roles that people could play when relating to a company.

Why is this a problem? Imagine that a store worker decides to buy products at her workplace. In this case, the worker will be behaving like a customer. An unsuitable although very frequent solution to this is to create a second record for the worker as a customer, as if she was a different person. Consequently, the same person would have two records in the system: one as a worker and another as a customer. This produces data redundancy, and it is a source of data inconsistency, because, for example, if the worker record changes her address, the related customer record may keep the old address. Therefore as they are the same person, this information is inconsistent.

A more suitable solution is to consider that there exists a Person that may relate to a Company in at least two ways: as a customer and as a worker. The specific properties of a customer (credit limit, for instance), and of a worker (salary, for instance), would be properties of the associations and not of the person. To represent these association properties, an association class can be defined for each one, as shown in Fig. 9–17.

Therefore when the same object may play different roles related to other objects, these roles should not be represented as subclasses, but as association classes.

**Figure 9–16: Unsuitable way of using inheritance when roles should be the case.** *(p. 156)*

> **Diagram content (transcribed from the figure image):** AVOID ("Roles are not subclasses"): Person {id, name, address, phone} with subclasses Worker {+wage: Money} and Customer {+credit_limit: Money}; Customer 1 — * Order {«imm» «unique» +number: OrderNumber; +value: Money}.

**Figure 9–17: Concepts being represented as association classes.** *(p. 156)*

> **Diagram content (transcribed from the figure image):** Roles modelled as association classes: Person * worker — working_place * Store {+id: StoreID; +name; +address} with association class Worker {+wage: Money}; Person * customer — shop * Store with association class Customer {+credit_limit: Money}; Customer 1 — * Order {«imm» «unique» +number: OrderNumber; +value: Money}.

To decide which situation demands inheritance and which situation demands association classes, it may be verified if the “subtypes” depend on the existence of a third class to make sense. If the “subtype” depends on a third class, then the solution consists of using an association class. For example, nobody may be simply an employee; if someone is an employee, then she must be associated to a company or at least to a boss.

Thus it is unsuitable to create classes that represent kinds of people that are not subclasses, but roles. Workers, teachers, students, principals, customers, etc., should not be subclasses of Person. Concepts like these only make sense if related to other concepts such as Company, School, and Department. A person may be worker at a company, student at a school, etc.

The difference between using an association class and an intermediary concept is subtle. Fig. 9–18 shows an example of a reservation being modeled as an intermediary concept (up) and as an association class (down).

In the case of Fig. 9–18 (up), a reservation associates a person to a flight. In the case of Fig. 9–18 (down), the person and the flight are directly associated, and the reservation is an association class.

**Figure 9–18: A reservation being modeled as an intermediary class and as an association class.** *(p. 157)*

> **Diagram content (transcribed from the figure image):** Two equivalent forms: Person 1 — * Reservation * — 1 Flight (reservation as intermediate concept) vs Person * — * Flight with association class Reservation.

However, those representations are not equivalent. If an association class is used, then one person may have only one and just one reservation for a given flight. In the other case, the customer can have many reservations to the same flight.

## 9.3 Modal classes

*Chapter 9 · p. 157*

Modal classes are used to model concepts with instances that can change from one state to another during their existence, changing, possibly, their properties’ structure, including attributes, associations, and behavior. Although a few programming languages allow instances to change their structure by changing their class, this is not assumed as a modeling principle because such changes may create unpredictable structural problems and are usually unsafe.

Even if an instance could change its class, redefining its attributes and associations remains a problem. However, there are modeling techniques that allow to represent situations that would need objects that change class without using this feature. The idea is not to change the object class, but its state. For example, when a sale is paid, it does not become a new type of sale: it just changes its state.

Three increasingly complex situations related to state modeling may be identified:

- Stable transition: The different states of an object do not affect its structure, but only its property values (attributes and links). For example, a state may be represented by a single attribute.

- Monotonic increasing transition: As the object changes state, it may only keep its properties or acquire new ones. Associations and attributes can be gained, but not lost.

Nonmonotonic transition:^3 As the object changes state, it may keep, acquire, or lose properties. Associations and attributes may be gained and lost.

3 The monotonic decreasing case can be considered here too (a transition that can only remove properties from an instance).

Modeling solutions for the stable and monotonic increasing transitions are quite simple. However, for modeling the nonmonotonic transition, a design pattern named State (Gamma et al., 1995) is necessary, as seen in the following subsections.

### 9.3.1 Stable transition — 9.3 Modal classes

Frequently, different states of an object may be represented by a simple attribute. In fact, the set of all attributes and links of an object defines its state. For example, the state of an order could be modeled simply as a state attribute typed with an enumeration whose values may be “ongoing,” “concluded,” and “paid.” (Fig. 9–19).

The transition is considered stable because just the value of the attributes can change. The inner structure of the object is kept the same. This does not happen with the two cases presented in the next subsections.

If all attributes are immutable, then the object cannot change state and behaves like a more complex constant.

### 9.3.2 Monotonic increasing transition — 9.3 Modal classes

The situation is a bit more complex when the concept may acquire new attributes or associations as it changes state. For example, invoices that are waiting for payment have only due_date and due_value as attributes. But an invoice that is paid additionally has payment_date and paid_value (Fig. 9–20).

It is said that the transition in Fig. 9–20 is monotonic increasing because new attributes and associations may be created for it, but not eliminated. This implies that a paid invoice cannot go back to be a new invoice again.

One solution that could be used in this case is to consider that the attributes that would be added after the object is created are optional, meaning that they can remain undefined until the invoice is paid. Fig. 9–21 shows optional attributes marked with the stereotype «opt». Although it may be a popular solution, it brings problems. First, it is necessary to assure that when payment_date is defined, paid_value would be too, and vice versa. An invariant could do the trick, if the team knows how to use them.

But this model is still not good because it generates a class with low cohesion, which has, in consequence, consistency rules that should be checked frequently. This kind of class is highly susceptible to programming errors.

**Figure 9–19: An example of a class with stable state transition.** *(p. 158)*

> **Diagram content (transcribed from the figure image):** Order {«imm» «unique» +number: Natural; «imm» +date: Date; «imm» +value: Money; +state: OrderState}; «enumeration» OrderState {ongoing, concluded, paid} — state as an attribute.

**Figure 9–20: A class with monotonic increasing transition.** *(p. 159)*

> **Diagram content (transcribed from the figure image):** Transient/modal classification problem: NewInvoice {«imm» +due_date: Date; «imm» +due_value: Money} becomes (arrow) PaidInvoice {«imm» +due_date; «imm» +due_value; +payment_date: Date; +paid_value: Money} — an object would need to change class.

**Figure 9–21: A class with optional attributes and cohesion problems.** *(p. 159)*

> **Diagram content (transcribed from the figure image):** AVOID ("This class has cohesion problems"): Invoice {«imm» +due_date; «imm» +due_value; «opt» +payment_date: Date; «opt» +paid_value: Money}.

It would be better to model the invoice concept so that the consistency of the objects could be constrained by the structure of the model itself and not by external rules. As it is a monotonic increasing transition, then it is possible to model this situation just by splitting the original concept in two: one that represents the invoice and another that represents its payment with the properties that were added when the payment occurred. These two concepts are, then, linked by a 1 to 0.1 association, as seen in Fig. 9–22.

Notice that in Fig. 9–22, the attributes that were optional before are now mandatory and immutable.

With the model presented in Fig. 9–22, it is impossible for an invoice to have a defined payment date and undefined paid value or vice versa. This is assured without performing any further verification on its attributes or associations.

We can still define the state of an invoice based on the existence or not of a payment. The state of an invoice can be, therefore, a derived attribute, which is calculated as follows: if there is no payment linked to the invoice, then the invoice is new; otherwise, it is paid. In OCL, that condition may be expressed as:

```ocl
Context Invoice::InvoiceState
    derive:
        if self.payment->isEmpty() then
            InvoiceState::new
        else
            InvoiceState::paid
        Endif
```

This expression would be associated to the diagram shown in Fig. 9–23.

**Figure 9–22: Effective way to represent monotonic increasing transition.** *(p. 160)*

> **Diagram content (transcribed from the figure image):** Better: Invoice {«imm» +due_date: Date; «imm» +due_value: Money} 1 — 0..1 Payment {«imm» +payment_date: Date; «imm» +paid_value: Money}.

**Figure 9–23: An invoice with a state as a derived attribute.** *(p. 160)*

> **Diagram content (transcribed from the figure image):** Same as 9–22 plus derived attribute Invoice +/state: InvoiceState and «enumeration» InvoiceState {new, paid} (state derived from existence of a Payment).

The expression above introduces two new OCL features:

- if-then-else-endif, which is one of the OCL selection functions and works like a ternary on programming languages. If the condition after the if is true, then the function results in the evaluation of the expression after the then; otherwise, it results in the evaluation of the expression after the else.

- isEmpty(), which is a function applied to a collection structure and returns true if the collection is empty and false otherwise. It is an easy way to check if there is some object linked to another object or not.

### 9.3.3 Nonmonotonic transition — 9.3 Modal classes

With nonmonotonic transition, an object may both gain and lose properties as it changes its state. Fortunately, it is not frequent that an information system requires any information to be lost. However, sometimes, that can be exactly what should be done.

For example, there are many ways to conceive and model a reservation system for a hotel. One of them consists of regarding the hosting as an entity that evolves from a reservation in three steps:

1. Initially, a potential guest makes a reservation indicating the days she intends to arrive and depart, the kind of accommodation, and the number of people. The hotel provides the fee.

2. When the guest checks in, the arrival date is registered (it may be the same date of the reservation or a different date). The hotel assigns a room that may be different from the one initially reserved if agreed and, if this is the case, it informs the guest of the new fee. The expected date of departure continues to exist, although it can be updated during the stay.

3. When the guest checks out, the expected departure date ceases to exist and the effective departure date is registered, and the bill must be paid.

This set of states may be modeled during business analysis with a state machine diagram like the one in Fig. 9–24.

If a hosting just acquires new attributes and associations as it evolves through the states of Fig. 9–24, then it could be represented by a chain of concepts such as Reservation/ CheckIn/ChechOut shown in Fig. 9–25.

However, although usually we do not want to delete information there can be situations in which this is required by law (e.g., if there are data protection laws), or simply it may appear to be the right thing to do.

Thus we will consider that in our example, when a guest checks in, the estimated arrival is not necessary anymore and that it should be removed from the information system. The same happens to the estimated leave, after check-out. One solution would be simply erasing the value of the attributes estimated_arrival and estimated_leave in class Reservation. But in this case, the attributes are kept existing. Only their value would be nullified, and as they cannot be immutable the possibility of redefining those attributes after the lodging in finished would remain. Thus we need a way to remove those attributes from the system, not only their values.

Maybe the better possibility to represent this kind of situation is to use a design pattern known as State (Gamma et al., 1995). According to this pattern, a class should be separated from its states. Properties that are shared by all states are kept in the original class, and properties that belong only to one or a few states are moved to the respective states. These states are specializations of an abstract class, as shown in Fig. 9–26. Wait? Is it not the case that HostingState is not generalizing any property? No, this class is generalizing the association with class Hosting.

**Figure 9–24: A state machine diagram modeling a simple hosting.** *(p. 161)*

> **Diagram content (transcribed from the figure image):** State machine of a lodging: ● —reserving→ Reservation —check in→ CurrentLodging —check out→ FinishedLodging → ◉ (a modal class whose instances pass through stable states).

**Figure 9–25: Possible model for reservations as monotonic increasing transitions.** *(p. 161)*

> **Diagram content (transcribed from the figure image):** Hotel model without states: Person {«imm» «unique» +id: ID; +name: String} 1 guest — * Reservation {+nrPeople: Natural; +fee: Money = accomodation_type.fee; +estimated_arrival: Date; +estimated_leave: Date}; Reservation * — 1 accomodation_type AccomodationType {+name: AccomodationDescription; +fee: Money}; Reservation 1 — 0..1 CheckIn {«imm» +check_in: Date} 1 — 0..1 CheckOut {«imm» +check_out: Date}; CheckIn * — 1 Room {+number: Natural}; AccomodationType 1 — * Room; «enumeration» AccomodationDescription {luxury, superior, honey_moon, presidential}.

In Fig. 9–26, the attributes nrPeople and fee exist in every possible state of a hosting, and this is why they are represented in the hosting Hosting class that separates a reservation from its state. The other properties are distributed among the three possible states:

- Reservation: A hosting, in addition to the number of people and fee, has estimated arrival and leaving dates and the accommodation type (not yet a room), from which the initial value for the hosting fee is obtained.

- CurrentLodging: A hosting, in addition to the number of people and fee, has an immutable check-in date, estimated leaving date, and a room assigned. The estimated_arrival attribute and the straight link to the accommodation type are not necessary anymore and do not exist in this state.

- FinishedLodging: A hosting, in addition to the number of people and fee, has immutable check-in and check-out dates, and a room assigned. The estimated leaving date is not necessary anymore and does not exist in this state.

From the point of view of a Room, it can now be linked to at most one CurrentLodging (0..1), but it can be associated to many FinishedLodging (– * ). This way, the temporal property of that association is already modeled too, because the association of a room to lodging may be at most one in the present, but many in the past.

**Figure 9–26: Nonmonotonic state transitions modeled with the State design pattern.** *(p. 162)*

> **Diagram content (transcribed from the figure image):** State pattern for the same hotel: Person 1 guest — * Hosting {+nr_people: Natural; +fee: Money = state.accomodation_type.fee}; Hosting 1 — 1 state HostingState (abstract) with subclasses Reservation {+estimated_arrival; +estimated_leave}, CurrentLodging {«imm» +check_in: Date; +estimated_leave: Date}, FinishedLodging {«imm» +check_out: Date; «imm» +check_in: Date}; Reservation * — 1 accomodation_type AccomodationType {+description: AccomodationDescription; +fee: Money}; AccomodationType 1 — * Room {+number: Natural}; CurrentLodging 0..1 — 1 Room; FinishedLodging * — 1 Room; same AccomodationDescription enumeration.

## 9.4 Invariants

*Chapter 9 · p. 163*

There are situations where the expressivity of the diagrams is not enough to represent rules that should be recorded in the conceptual model. In some of these cases, the team should use invariants.

Invariants are general constraints over all instances of a given class. Some constraints are represented in the association roles when a multiplicity different from “– * ” is used.

However, not every possible constraint may be represented in the association roles. Consider the model shown in Fig. 9–27 that represents a situation in that a student may be registered in different courses, but the maximum limit is not the number of courses, but the number of weekly hours.

The maximum number of hours of a career may be represented as an attribute of the career, because it may be different for different instances of this class. Any course in this career has its number of hours, and the number of hours spent by a student is the sum of the number of hours of the courses he is registered in. The invariant is represented close to the name of class Student. It is the abbreviated form of the following OCL expression:

```ocl
Context Student
    inv:
        self.courses->sum(:a_course|
            a_course.hours
        ) <= self.career.max_hours
```

The expression “sum” in OCL is an operation that can be applied to collections. For each element in the collection, it evaluates the expression between parenthesis, which must denotate a numeric value, and produces the summatory of those values. If there is no expression between parenthesis, then it considers that it is being sent to a collection of numbers and proceeds to their summation. Thus the expression courses- . sum(hours) could be, in principle, also written as courses.hours- . sum(). However, as the default collection in OCL is the set, the result, in this case would not be correct, because a set does not allow a value to be repeated. Thus if there are two or more courses with the same number of hours, only one occurrence would be added to the sum.

**Figure 9–27: An example of a class with an invariant.** *(p. 163)*

> **Diagram content (transcribed from the figure image):** Invariant: Career {+name: String; +max_hours: Natural} 1 — * Course {+name: String; +hours: Natural}; Career 1 — * Student {+name: String; «imm» «unique» +id: ID}; Course * — courses * Student; Student carries the invariant {courses->sum(hours) <= career.max_hours}.

Another solution to this problem is to convert the set into a bag before taking the hours. OCL has messages to convert data structures, and in order to convert any other collection into a bag, the message “asBag()” may be used. Thus the expression can also be represented correctly as: courses - . asBag().hours- . sum().

Observe that the invariant declaration in OCL does not have a subcontext; it must be true for every instance of the class, not for a particular attribute or association role.

Many software developers, when faced with the need to use constrains such as invariants, choose to incorporate these rules in methods that update the attributes and links of the objects. However, this approach may be riskier and more laborious.

The model presented in Fig. 9–27, however, may still have a problem. As it is, it allows a student to register in any course, no matter which career it belongs. If the business rule states that a student must only register in courses belonging to her career, another invariant should be used. A first approach to it could be something like:

```ocl
Context Student
    inv:
        self.courses.career=self.career
```

The expression uses a feature of sets (not allowing elements to be repeated) to verify that all courses taken by the student belong to the student’s career. The expression self.career results in the student’s career (a set with a single element because of the multiplicity of the role from student to career). On the other hand, the expression self.courses.career results in the set of all careers associated to all courses taken by the student. If there are courses from different careers, then that set could not be equal to self.career (which has a single element). Otherwise, if all careers are the same, then the set self.course.career will contain a single element (because sets do not repeat elements). If that element is the same as self.career, then the invariant will be true and valid.

However, this expression is still incomplete, because if the student is not registered in any course, the expression self.courses will result in the empty set and therefore, self.courses.career will also be an empty set and so, different from self.career. To resolve this, a ternary can be used:

```ocl
Context Student
    if self.courses->isEmpty() then
        True
    else
        self.courses.career=self.career
```

## Questions (Chapter 9)

1. Try to imagine a real-world situation where the right structure to be used is a sequence. Remember that a real sequence allows elements to be repeated and assigns position to elements. Try not to get fooled by natural language use of the word “list.” A “grocery list,”

for example, is not a sequence, because elements do not repeat and their position is irrelevant. Also, a student roll call may be organized in alphabetical order, but again, repetition is not allowed, and the order is again irrelevant although convenient for searching. Thus those are not real sequences.

2. Elaborate a list of concepts and subconcepts (subtypes of the original concept, e.g., dog and beagle) from common sense. Then, try to identify the type of each relation: structural, associative, or temporal. Try to have at least one example of each type in your list.

3. Try to elaborate three real-world examples of map, partition, and relation.

4. What is the difference between using an association class and an intermediate class?

5. Try to develop a real-world model that needs an invariant to be correct.

This page intentionally left blank

