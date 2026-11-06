<!-- Knowledge file: Chapter 13 — Domain tier design -->
> **About this file.** Chapter 13 of a cleaned, AI-ready edition of Wazlawick, R. S. (2024). Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-443-13739-6.  
> **Covers:** Domain tier design: visibility (association, parameter, local, global), dynamic models from contracts, delegation vs concentration, design class diagram.  
> **Use this file when:** turning contracts into object interaction (communication/sequence) diagrams and a design class diagram.  
> **Sections:** 13.1 Introduction to domain tier design (p. 247); 13.2 Object responsibility distribution (p. 251); 13.3 Visibility (p. 254); 13.4 Dynamic modeling based on postconditions (p. 267); 13.5 Delegation and low coupling (p. 276); 13.6 Design class diagram (p. 277)  
> **Contains:** 35 figures transcribed as text, 10 code listings.

# Chapter 13: Domain tier design

*Source: Wazlawick, Object-Oriented Analysis and Design for Information Systems, 2nd ed. (Elsevier, 2024), starts p. 247*

Key topics in this chapter

- Responsibility

- Visibility

- Low Coupling

- Delegation

- Dynamic Modeling

- Design Class Diagram

## 13.1 Introduction to domain tier design

*Chapter 13 · p. 247*

Software design in general aims to produce a solution to a problem that has already been sufficiently clarified by analysis. The static aspects of the problem are represented in the conceptual model, and the functional or transformational aspects are represented in the expanded use cases, system sequence diagrams, and system operation contracts. Now it is time to design a solution to implement the logical and technological aspects of the system. In this sense, design is a solution for a problem modeled by analysis.

During iterations, after expanding use cases, refining the conceptual model, and writing contracts, the team may conduct design activities, which can be divided into two groups:

- Logical design (this chapter), which includes the aspects of the problem that are related to the business logic. Usually, the logical design is represented in the design class diagram (DCD), which evolves from the conceptual model, and by interaction diagrams, which show how objects exchange messages to perform system operations and achieve the postconditions of the contracts.

- Technological design, which includes all aspects of the problem that are inherent to the technology used: interface, data storage, security, communication, fault tolerance, etc. Some activities related to technological design are addressed in this book:

- Interface tier design (Chapter 16), which consists of designing the user interface and preferably keeping it decoupled from the domain tier.

- Persistence tier design (Chapter 17), which consists of the definition of a persistency mechanism to allow data load and save, which can be performed automatically, preventing the designer from being overconcerned about those aspects.

Logical design is also known as domain tier design. The domain tier corresponds to the set of classes that perform all data transformation and queries. Other tiers implement technological aspects of the system: persistency, interface, communication, security, etc. They 

249 are usually derived from and dependent on the domain tier, and their utility is to connect the pure logic of the domain to the physical computer aspects (communication networks, human interfaces, storage devices, etc.).

The design of the domain tier consists basically of two activities that can be performed iteratively:

- Dynamic modeling, which consists of building execution models for the system operation contracts. In object-oriented systems, such models are usually represented by interaction diagrams such as communication or sequence diagrams or even as pure text algorithms.

- DCD building, which consists basically of adding to the conceptual model, some information that was not possible or desirable to obtain earlier, such as the association’s navigation direction, and the methods to be implemented in each class. Those aspects can be effectively included in the software design if dynamic modeling is done. Additionally, the structure of design classes may be a little different from the conceptual model as new classes or a different class organization may be necessary to perform some concrete functions that will be required at this point.

The logical design can be performed systematically if the team is in possession of two artifacts:

- The evolving conceptual model that will be converted into the DCD.

- The functional model represented by system operation contracts.

The logical design activities consist of building interaction diagrams for system operations found in the system sequence diagrams, considering the DCD and the respective system operation contract.

Dynamic modeling, as mentioned before, can make use of communication or sequence diagrams, or even algorithms. Each of those forms has advantages and disadvantages:

- Algorithms, for programmers, are easier to write, but it may be difficult to clearly realize the connections among objects in simple text. Thus the choice for algorithms to use object-oriented dynamic modeling may raise the risk of high coupling among classes, generating bad design. One of the worst results of the common use of this tool is that programmers tend to write methods as if they are using 1970s structured programming and not object-oriented programming.

- Communication diagrams are better than algorithms for visualization and responsibility distribution purposes, and they are better than sequence diagrams for providing an explicit view of the visibility lines between objects. However, these diagrams may be difficult to organize and in the case of complex collaborations, they may become harder to read than sequence diagrams. Maybe because of that, the OMG is not evolving the chapter dedicated to communication diagrams in the UML handbook.

- Sequence diagrams are usually easier to read than communication diagrams, but they do not show explicitly the visibility lines between objects. If the designer is not vigilant, invalid or impossible communications may be included in the diagram. However, as it is

the most used interaction diagram of UML and the fact that we already used them to systematize use cases, this will be our choice in this chapter given that they are always used with one eye in the conceptual model or DCD.

Thus this chapter uses sequence diagrams for dynamic modeling in order to ease the visualization of the communication between objects.

The class diagram examples in this chapter assume that it is design time. Thus associations may be directed, and classes may have methods and private attributes.

The chapter initially discusses object responsibility, which is a key concept in understanding how to distribute methods among objects. Knowing which object should implement which responsibility allows design classes to be highly cohesive.

Another key concept that is presented in detail is visibility, which establishes that communication among objects can occur only when visibility lines exist. If the quantity of those lines is minimized, low coupling (Meyer, 1988) is achieved in the design.

Finally, the chapter explains how to transform contracts into dynamic models by using responsibility distribution and visibility, as well as other design patterns, to produce the best design possible.

## 13.2 Object responsibility distribution

*Chapter 13 · p. 251*

Responsibility distribution among objects has to do with the following question: What methods must be implemented in which classes?

Many designers find it difficult to build an elegant solution to that problem when they simply try to add methods to a class diagram. The use of interaction diagrams and design patterns may, however, provide a more efficient and effective way to discover the most suitable place to implement each method.

The DCD is built from the conceptual model, which provides the basic set of classes, attributes, and associations that are needed. Then, it is necessary to develop interaction diagrams for each system operation contract; not necessarily everyone the just one sprint, because this can be done iteratively and cumulatively. Those diagrams show objects exchanging messages to achieve the postconditions of the respective contracts. There are techniques that help in building those diagrams in an elegant way. The use of diagrams is better than algorithms, especially for novice designers, because with algorithms, the designer may fall for the temptation of concentrating all responsibilities in a single class, while the diagrams allow better visualization of the distribution of responsibilities among the objects. An example of that situation is presented later in this chapter.

When a team builds object-oriented code without an adequate method for dynamic modeling (that is, simply making a class diagram and adding ad hoc methods to it) there is a risk that the responsibilities may be poorly distributed among the classes, and the result may be as unstructured as the old spaghetti code. Usually, object-oriented systems are well organized at the class level, but unhappily the code written inside methods is often poorly designed.

Thus for a system to be elegant, responsibilities must be well distributed. If a systematic method is not used, responsibilities can become concentrated in the controller class, or in classes that represent business actors, such as Person or Company. In the end, classes such as Project, Assessment, and Payment would have no relevant method besides their own attribute’s getters and setters.

When one or two classes do all the work, and others are passive, there is no objectoriented code worthy of that name, but a concentrating structure.

On the other hand, designers, sometimes, make the mistake of believing that an objectoriented system is a simulation of the real world. But that is not usually true. An objectoriented model represents the information about the real world and not the things themselves. The difference is subtle: methods do not correspond to real-world action, but to the internal information processing of the system. That is why concepts such as Project that are passive in the real world may perform commands in object-oriented systems.

Thus designing object-oriented software must be understood as a precise method, guided by learned patterns, and not simply as the act of creating classes and associating ad hoc methods to them.

Before explaining how to distribute responsibilities among objects, a taxonomy of those responsibilities will be defined. Basically, there are two high-level groups of responsibilities:

- The responsibility of knowing, which corresponds to the getters or queries on objects.

- The responsibility of updating, which corresponds to the commands performed by objects, set in the case of attributes, add, remove, and replace in the cases of roles, and nonpattern others.

Both high-level groups are divided into three subgroups:

- Things that the object knows or updates within itself (getting and setting its attributes).

- Things that the object knows or updates in its neighborhood (adding, removing, and replacing its links).

- Other things that the object knows or updates that are not classified in the previous two groups. Normally these things correspond to derived knowledge (derived attributes and associations, and other queries in general) and coordinated activities (delegate methods).

In the case of the responsibilities of knowing, the three subgroups could be characterized as follows:

- Things that the object knows about itself: This is equivalent to being able to access the attributes of an object. Such responsibilities are incorporated to the classes by basic query methods named with the prefix get followed by the name of the attribute.^1 For example, if the class Person has an attribute birth_date, then the method get_birth_date has the responsibility of knowing the value of that attribute.

> *Footnote 1:* That is valid for normal attributes belonging to classes of the conceptual model, though. During the construction of the DCD, new design attributes that represent the internal state and influence the behavior of an object may become necessary and those attributes do not necessarily have to be accessed by other objects: in that case, they should not have getters (they are private or protected).

- Things that the object knows about its neighborhood: This is equivalent to being able to access directly linked objects. This responsibility is incorporated in the methods that obtain the set of objects linked through a given role. Such methods are usually prefixed with get and followed by the role name (or the name of the class in the absence of the role name). For example, if Car is associated to Person and the role name for Person is driver, then the method get_driver returns the set of people that are drivers of a given car it may be zero person, one person, or more.

- Derived things that the object knows: This is equivalent to information that is composed or calculated from other information. This responsibility may be associated to derived attributes and derived associations, in which case the methods are also prefixed by get followed by the name of the derived attribute or association. For example, if total_value is the name of a derived attribute of class Order, then get_total_value is a method that returns that derived attribute. Derived knowledge also includes other queries about an object that cannot be represented as derived attributes or associations, such as queries with parameters; in that case, names may vary.

In the case of responsibilities related to updating information, the three subgroups could be characterized as:

- Things that the object does over itself: This corresponds to the basic command that updates a single attribute, which is prefixed with set,^2 followed by the attribute name. For example, if the class Person has an attribute weight, then set_weight is a method that incorporates the responsibility of changing that attribute.

- Things that the object does over its neighborhood: This corresponds to the basic commands that add, remove, and replace links between objects. These commands are identified respectively by the prefixes add, remove, and replace followed by the name of the association role. For example, if the class Customer has an association with Reservation, the methods add_reservation, remove_reservation, and replace_reservation incorporate that responsibility.

- Things that the object coordinates: This corresponds to commands that perform multiple tasks, possibly in different objects. These commands are known as delegated methods, and they are crucial for class design because the methods of the other groups are just basic commands with previously known behavior; but delegate methods must be designed for created nonbasic behaviors. For example, if all the products in a given order must be marked as delivered, the coordination of the marking activities must be made by the instance of Order itself, because it is the object with the most immediate access to the objects that participate at the operation.

**Table 13–1: summarizes the six kinds of responsibilities and the methods typically associated to each kind.**

> *Footnote 2:* Remember that not every attribute may have a setter. Immutable attributes should not have a setter. Derived attributes never have setters, and private attributes also should not have public setters.

**Table 13–1: Object responsibilities.**

||Know|Update|
|---|---|---|
|About itself|Query on attributes: – get_attribute()|Update attributes: – set_attribute()|
|About its neighborhood|Query on association roles: – get_role()|Update links: – add_role() – remove_role() – replace_role()|
|Others|Queries on derived attributes and roles, and other general queries: – get_attribue() – get_role() – names vary in the case of other general queries|Delegated methods: – names vary|

There is no standard name for delegated methods and general queries, which are named depending on the operation they perform. Usually, these names must not include the name of the class where they are implemented. For example, if Decision implements a command to finish it, do not name it as a_decision.finish_decision(); it is better not to mention the name of the class in the method. Then, a_decision.finish() would do it better.

## 13.3 Visibility

*Chapter 13 · p. 254*

For two objects to be able to exchange messages to perform their responsibilities, it is necessary that some kind of visibility exists between them. There are four basic forms of visibility between objects:

- By association: If there is a link between two objects defined by an association between their classes.

- By parameter: If an object, when performing a method, receives another object as parameter.

- Locally declared: If an object that is performing a method receives another object as a query return.

- Global: If an object is visible by any other object.

None of the visibility forms are necessarily symmetric. That is, if x has visibility to y that does not mean that y necessarily has visibility to x. Visibility by association may be symmetric if the association is bidirectional, but this is not always the case.

### 13.3.1 Visibility by association — 13.3 Visibility

There is visibility by association between two objects only when there is an association between their respective classes. The kind of visibility allowed depends on the role multiplicity and other features, such as the association being qualified, ordered, and so on.

**Figure 13–1: Unidirectional association between classes with multiplicity 1.** *(p. 255)*

> **Diagram content (transcribed from the figure image):** One-way association to 1: Payment —× (not navigable back) → 1 Order.

**Figure 13–2: Object visibility to a single object.** *(p. 255)*

> **Diagram content (transcribed from the figure image):** Delegation through association to 1: :Payment sends a_date = get_date() to :Order.

An association role may be considered a collection of instances, especially if its upper bound is greater than 1. But, in the case of multiplicity 1 or 0.1, it is possible to interpret the role as a set or as an individual object. OCL, in these cases, considers the role both as an object and a collection. Regarding multiplicity, then, the following kinds of visibility may be identified:

- If the multiplicity is 1, then there is straight visibility to one instance and to the set that contains that instance.

- Any other multiplicity allows only visibility to a set of instances^3 .

The DCD is not the only specification that determines the multiplicity of a role. It is complemented by the preconditions of the contracts, which can constrain multiplicity bounds even more, as seen in the following sections.

### 13.3.1.1 Visibility to a single object — 13.3 Visibility

Fig. 13–1 shows a Payment class that has a unidirectional association to Order with multiplicity 1. In this case, any instance of Payment has straight visibility to an instance of Order.^4

In this way, when an instance of Payment is represented in an interaction diagram, as shown in the sequence diagram in Fig. 13–2, it can send messages directly to the instance of Order that is linked to it.

> *Footnote 3:* It could be considered that a 0..1 role is filled with a single object or a null value. However, that is not coherent with the interpretation of other multiplicities such as, for example, 0..2 or– , where 0 stands for the empty set and not for the null value. To avoid such inconsistency it is preferable to consider that multiplicity 0..1 refers to a set that can be empty or contain a single element.

> *Footnote 4:* And additionally, to a set that contains that order.

**Figure 13–3: Unidirectional association between classes with multiplicity– .** *(p. 256)*

> **Diagram content (transcribed from the figure image):** One-way association to many: Order —× → * items Item.

**Figure 13–4: An object with visibility to a set of objects sending a message to the set structure.** *(p. 256)*

> **Diagram content (transcribed from the figure image):** :Order sends x = isEmpty() to the collection items : Set<Item>.

### 13.3.1.2 Visibility to multiple objects — 13.3 Visibility

Multiplicity values different from 1, such as– x , 1.– , 0.1, or 5, provide visibility to a collection^5 of objects, not just to a single instance. From now on, all those cases will be generally addressed as– * multiplicity, or association to many.

- * Fig. 13–3 shows class Order with a unidirectional association with multiplicity– to class Item. In this case, an instance of Order can send a message to a set of instances of Item. It is possible to send messages to the set structure itself,^6 as shown in Fig. 13–4. In the example, the message verifies if the set is empty.

But it is possible to send a message iteratively to each element of the set, as shown in Fig. 13–5. In the example, the message requests the subtotal value of each item.

Thus messages, in sequence diagrams, may be addressed to the collection structure or to the collection elements individually. When a message is sent to the structure, the type of the object that receives the message should be a collection, such as Set , Item. in Fig. 13–4. The fact that the message is iterative and sent to all elements in the set is represented by the loop fragment that involves the message. The condition [for all] indicates that all elements of the set receive the message.

A filter could be used here if the message was intended just for some selected elements. For example, if the message get_subtotal is intended only for items with quantity greater than 1, then the condition into the loop fragment could be written as item|item.quantity . 1, instead of for all. Thus it is identical to the OCL expressions used inside parentheses of the select operation.

> *Footnote 5:* A set by default.

> *Footnote 6:* In this text it is assumed that the operations available for sets and other collections are the ones defined by OCL (Object Management Group, 2010). However, if different languages or packages are used, a different set of operations would be available.

### 13.3.1.3 Visibility by association with ordered roles — 13.3 Visibility

If the association role is ordered with the use of the {ordered} or {sequence} constraints, the visibility to the collection as a structure is kept, but additionally straight visibility to individual elements indexed by their position is allowed.

Fig. 13–6 presents a class diagram with a unidirectional association with an ordered role. In Fig. 13–7, different types of visibility allowed by that association are shown.

**Figure 13–5: An object with visibility to a set of objects sending a message to each element of the set.** *(p. 257)*

> **Diagram content (transcribed from the figure image):** :Order with a loop [for all] sending an_ammount = get_subtotal() to each element of items : Set<Item>.

**Figure 13–6: Unidirectional association between classes with ordered multiplicity.** *(p. 257)*

> **Diagram content (transcribed from the figure image):** Person —× → * {ordered} orders Order.

**Figure 13–7: Different types of visibility allowed by ordered or sequence roles.** *(p. 257)*

> **Diagram content (transcribed from the figure image):** :Person with orders : OrderedSet<Order>: x = getSize(); loop [for all] a_date = get_date(); some_date = get_date(3) (access by position in an ordered collection).

In Fig. 13–7, the first message is sent to the OrderedSet structure as a whole and asks how many elements there is in the OrderedSet. The second message is enclosed in a loop fragment and corresponds to asking each Order in the OrderedSet its date. The third message is a new type when compared to the other situations seen above, it accesses a given element in the OrderedSet by its index. In this case, it returns the date of the element in position “3.” If there is no element in this position, then it returns the empty set.

### 13.3.1.4 Visibility by association with qualifiers — 13.3 Visibility

If the association is qualified as a map (only one element for each value of the qualifier), there are at least two forms of elements visibility:

- Visibility to the set of elements (as if it were a regular set).

- Visibility to a single element if the object has a key to access the element in the association role.

Fig. 13–8 presents a class diagram with a qualified association from Person to CreditCard.

Fig. 13–9 shows that the structure as a whole can be addressed. It shows also that all elements of the role can be accessed just as if the qualified association has a set in the opposite role. It also shown that if the origin class has one of the keys for the mapping, then it can access one object directly.

It is also possible that the qualified association represents a partition. In this case, there is no way to access one element directly, but only the complete set or the subsets of the partition. Fig. 13–10 shows a link that defines a partition. Card numbers are immutable and unique, but card flags are just immutable. A person can have more than one card with the same flag. Thus this example defines a partition.

**Figure 13–8: Unidirectional association between classes with qualifier.** *(p. 258)*

> **Diagram content (transcribed from the figure image):** Qualified association: Person with qualifier number —× → 0..1 credit_cards CreditCard {«imm» «unique» +number: CreditCardNumber}.

**Figure 13–9: Different types of visibility allowed by qualified associations.** *(p. 258)*

> **Diagram content (transcribed from the figure image):** :Customer and the collection : Set<CreditCard>: x = size(); loop [for all] a_number = get_number(); a_date = get_validity(a_credit_card_number) (access by key).

**Figure 13–10: Unidirectional association between classes with qualifier defining a partition.** *(p. 259)*

> **Diagram content (transcribed from the figure image):** Partition: Person with qualifier flag —× → * credit_cards CreditCard {«imm» «unique» +number: CreditCardNumber; «imm» +flag: CreditCardFlag; «imm» +validity: Date}.

**Figure 13–11: Different types of visibility allowed by qualified associations that define partitions.** *(p. 259)*

> **Diagram content (transcribed from the figure image):** :Person with credit_cards : Set<CreditCard> and credit_cards : Set<CreditCard>["Visa"]: x = size(); loop [for all] date = get_validity() over all cards; loop [for all] date = get_validity() over the "Visa" partition only.

In this case, the whole set may be accessed. But the use of the qualifier allows also accessing cards belonging to a given subset. Fig. 13–11 shows the modes available.

In this figure, the first message accesses the structure as if it was a simple set. The second message is sent to each element of the whole set. The third message is sent only to a subset in which flag is equal to “Visa.”

### 13.3.1.5 Visibility by association with association class — 13.3 Visibility

As explained before, when a link with an association class is added, an instance of the association class is created and attached to the link. When the same link is removed, then the respective instance of the association class is destroyed. Thus if Person has a unidirectional association to Organization and that association has an association class Job, as shown in Fig. 13–12, when a link between instances of Person and Organization is added, an instance of Job is created; and every time a link from Person to Organization is removed, the respective instance of Job is destroyed. Therefore an instance of Person has visibility to two sets^7 with the same size: one with instances of Organization, and another with instances of Job. As it is a unidirectional association, an instance of Job has visibility only to a single instance of Organization.

**Figure 13–12: A unidirectional association with an association class.** *(p. 260)*

> **Diagram content (transcribed from the figure image):** Association class: Person —× → * work_place Organization, with association class Job.

**Figure 13–13: Two types of visibility that a class has when a unidirectional association has an association class.** *(p. 260)*

> **Diagram content (transcribed from the figure image):** :Person with workplace : Set<Organization> and : Set<Job>: loop [for all] an_address = get_address() on organizations; loop [for all] a_wage = get_wage() on jobs.

If the association in Fig. 13–12 were bidirectional, then an instance of Organization would also have visibility to a set of Person and a set of Job. Additionally, any instance of Job would have visibility to one instance of Person and one instance of Organization.

It is important to highlight that if the association is bidirectional, there is only one instance of Job attached to the link, not two.

Fig. 13–13 shows two kinds of visibility from the point of view of Person. The first represents the visibility that an instance of Person has to the set of instances of Organization as work places. That corresponds to the default visibility obtained for a role with multiplicity– .

> *Footnote 7:* The association probably would be physically implemented not as two sets, though, but by a dictionary. Here the visibility means that two sets of objects may be obtained by an instance; this does not mean that they are implemented like that.

The second one represents the visibility that an instance of Person has to a set of instances of Job, the association class.

The association class also works as a mapping in a way that is very similar to the qualified association. The qualified association maps an alphanumeric into an object, but an association with association class maps an instance into another instance. The model in Fig. 13–12 is equivalent to mapping a job for each organization a person works for. Thus if an instance of Person has visibility to a specific instance of Organization (key), it may find the correspondent instance of Job (value) as illustrated in Fig. 13–14.

Also, in Fig. 13–14, we can see that an_organization must be an instance of Organization and that the instance of Person must have some kind of visibility to it in order to use it to access the respective instance of Job. In the example, we used an instance of SomeClass to return an_organization to Person such that the necessary visibility is achieved.

Finally, Fig. 13–15 shows the visibility that instances of the association class have to the instances of the link participating classes: a visibility that is strictly one.

**Figure 13–14: An instance of a class in the origin of a unidirectional association that has visibility to an instance on the other side also has visibility to the corresponding instance of the association class.** *(p. 261)*

> **Diagram content (transcribed from the figure image):** :Person obtains an_organization = get_an_organization() from :SomeClass, then a_job = get_job(an_organization) from work_place : Set<Organization> (navigating from the association end to the association class).

**Figure 13–15: Instances of association classes have visibility to a single instance at the destiny (if unidirectional) or both ends of the respective link (if bidirectional).** *(p. 261)*

> **Diagram content (transcribed from the figure image):** :Job sends an_address = get_address() to :Organization (association class navigates to its participant).

### 13.3.1.6 The influence of preconditions on visibility by association — 13.3 Visibility

When a precondition in a contract states a multiplicity that is more restrictive than the one allowed in the class diagram, it is the visibility established by the precondition that must be considered in the context of that operation.

For example, consider the class diagram of Fig. 13–16, which defines that an order may or may not have a payment linked to it.

Consider now that a given operation contract has a precondition that states:

```text
pre:
    anOrder.payment->notEmpty()
```

Or:

```text
pre:
    anOrder.payment->isEmpty()
```

Then, both contexts are restricting the explicit multiplicity of the class diagram. In the case of the first precondition, the team must consider that the multiplicity in the Payment role is 1, as shown in Fig. 13–17.

In the case of the second precondition, the team must consider that the multiplicity in the Payment role is 0, as shown in Fig. 13–18.

In both cases, the new restrictions are only valid during the scope of the operation that has the specific precondition.

**Figure 13–16: A class diagram used in examples.** *(p. 262)*

> **Diagram content (transcribed from the figure image):** Order —× → 0..1 Payment.

**Figure 13–17: A precondition that makes an optional role mandatory.** *(p. 262)*

> **Diagram content (transcribed from the figure image):** Order —× → 1 Payment.

**Figure 13–18: A precondition that makes an optional role absent.** *(p. 262)*

> **Diagram content (transcribed from the figure image):** Order —× → 0 Payment (multiplicity zero: association temporarily forbidden/empty in this state).

### 13.3.2 Visibility by parameter — 13.3 Visibility

Visibility by parameter is obtained when an operation running in object A receives an object B as a parameter. In that case, the object A can communicate to B even if their classes are not associated.

Consider the example of Fig. 13–19, where the Product class has no association to the Delivery class. Therefore no instance of Product can send a message directly to an instance of Delivery or vice versa.

Consider now an instance of Order that is linked to one instance of Product and to one instance of Delivery as shown in Fig. 13–20. Now, consider that the instance of Order sends a message like register_weight to the instance of Delivery, passing a reference to the instance of Product (a_product) as an argument. Then, the instance of Delivery acquires visibility by parameter to that instance of Product.

Good design practice demands care with visibility by parameter. This is not the same kind of coupling that is obtained with visibility by association. With visibility by association, the participating classes are already coupled by a semantic association, that is, they are linked anyway because the meaning of one is attached to the meaning of the other (e.g., an order and its items). But in the case of visibility by parameter, any object may be passed as a parameter to another object, even if they have absolutely no relation between them.

**Figure 13–19: A model where a Product and a Delivery cannot communicate directly.** *(p. 263)*

> **Diagram content (transcribed from the figure image):** Order —× → * Product and Order —× → 0..1 Delivery.

**Figure 13–20: An object that should not be sending a message to a parameter.** *(p. 263)*

> **Diagram content (transcribed from the figure image):** Parameter visibility: :Order sends register_weight(a_product) to :Delivery; :Delivery then sends «parameter» any_message() to a_product : Product — note "Possible, but not recommended".

Each time a class declares methods with parameters belonging to other classes that are not yet associated, a new (and possibly unnecessary) coupling would be created. High coupling means poor design. Thus it is convenient to avoid that whenever possible.

The best use for visibility by parameter is to receive and resend objects until they reach the terminal (basic) operations. In practice, what happens is that certain objects will be passed to other objects in a chain until they reach some object that has association visibility to it and can therefore perform the required operation, as seen in Fig. 13–21.

In summary, objects received as parameter that have not association visibility to the object running the operation must not receive any messages; they can only be passed along as arguments. That would contribute to the low coupling principle that states that objects must keep the minimum possible links.

### 13.3.3 Locally declared visibility — 13.3 Visibility

Another form of visibility happens when an object sends a query to another and receives as return a third object. Fig. 13–22 shows the class diagram that serves as basis for this example and Fig. 13–23. Shows the objects communicating so that local visibility is created.

In the example, an instance of Person sends a message get_payment at position 1 to an ordered collection of Order. The person and the order are initially linked by association, but the person and the payment are not. However, after the get_payment method is performed, and an instance of Payment is returned to the person, it acquires local visibility to the payment, because, at that point, the payment is assigned to a local variable (a_payment) of the method the instance of Person is executing. From this moment on, the instance of Person acquires local visibility to the payment and may communicate directly with it.

**Figure 13–21: A chain of delegation.** *(p. 264)*

> **Diagram content (transcribed from the figure image):** Delegation chain (Law of Demeter style): :DeliverCompany → :Person product_damaged(p); :Person → :Order product_damaged(p); :Order → p : Product damaged().

**Figure 13–22: Class diagram used in example.** *(p. 264)*

> **Diagram content (transcribed from the figure image):** Person —× → * {ordered} orders Order —× → 0..1 Payment.

**Figure 13–23: Local visibility.** *(p. 265)*

> **Diagram content (transcribed from the figure image):** Local visibility: :Person gets a_payment = get_payment(1) from :OrderedSet<Order>, then sends «local» some_message() directly to a_payment : Payment — note "Possible, but not recommended".

**Figure 13–24: An object that creates another and receives its reference by local visibility that is transformed into association visibility.** *(p. 265)*

> **Diagram content (transcribed from the figure image):** :Order creates a_payment = Create() (dashed creation arrow to a_payment : Payment) then calls itself set_payment(a_payment).

However, a design pattern known as Don’t talk to strangers (Larman, 2004)^8 does not recommend that an object send messages to objects that are only locally visible. According to that pattern, the person should not send messages to a_payment. As seen before, there is always a design option that avoids this kind of communication. The problem here again is high coupling: if the person acquires local visibility to an instance of Payment, it acquires a link that is not semantically supported by the conceptual model. On the other hand, the price to pay for low coupling in this case is sometimes having to implement more delegate methods, as seen later.

An acceptable use for local visibility occurs when a basic command that creates an object is invoked. When an object is created, the new instance is usually referenced by a local variable. That local visibility may be immediately transformed into visibility by association, as shown in Fig. 13–24.

> *Footnote 8:* A summarization of the Law of Demeter (Lieberherr and Holland, 1989).

In the example, the message Create is a basic command, a constructor that produces the instance of Payment. At that moment, the instance of Order gets a new local visibility to it, through the local variable a_payment that contains the returning value of the command Create. The message set_payment links that new instance of Payment to the Order, which acquires visibility by association to it.

Here there are two important exceptions related to already mentioned design patterns: first, the command Create that modifies data can also return an object, but only if it is the object it created; second, an object is allowed to send messages to an object with local visibility because it was obtained from a method that specifically created it. Thus those exceptions refer to the patterns Query-Command-Separation and Do not speak to strangers.

Both local and parameter visibilities are valid only in the scope of the method that originated them; just like parameters and local variables in programming languages, they are only valid inside the methods where they have been declared. But visibility by association is more permanent, persisting until it is explicitly removed by a basic command that removes a link.

### 13.3.4 Global visibility — 13.3 Visibility

There is global visibility for an object when it is accessible by any object at any time. The Singleton design pattern (Gamma et al., 1995) suggests that an instance may be globally visible if it is the only instance of a class. This makes sense, because if that class has only one instance, it is not necessary to create associations from other objects to it. Also, if that class has a single instance, it is not necessary to pass it as an argument to a function because the idea with parameters is that they may vary, and that does not happen if the class has a single instance. Global visibility is the choice in this case.

Examples of singletons are classes that represent services, such as CurrencyConverter, TimeCounter, and OrderNumberGenerator. There must be a single instance of service classes that can be accessed by any object at any time. An example is shown in Fig. 13–25.

If the singleton pattern is overused, it may turn into an antipattern. Designers must not use singletons for entities of the conceptual model; for example, if the system is single user and a single order may exist at a time, it should not be declared a singleton because it is a conceptual entity, not a service class. A conceptual entity that is unique now may admit multiple instances in the future and declaring it a singleton would hinder the evolution of that class.

**Figure 13–25: An object with global visibility.** *(p. 266)*

> **Diagram content (transcribed from the figure image):** Global visibility: :Order sends «global» a_date = today() to «singleton» : Date.

Also, a singleton, in principle, should not have direct references to entities, because that reduces its reusability potential and creates high coupling problems. Service classes, such as Date, must not be associated to entity classes; they are globally visible and grant access to every instance.

## 13.4 Dynamic modeling based on postconditions

*Chapter 13 · p. 267*

We saw that system command contracts present a set of postconditions that correspond to certain basic commands for creating and deleting instances, adding, removing, and replacing links, and modifying attribute values. These contracts only indicate what is supposed to happen, but they do not show how messages are exchanged between objects to achieve those goals. UML interaction diagrams may be used to exactly design how these collaborations may happen. The following principles are recommended:

- The kind of visibility among objects depends fundamentally on the role features, such as multiplicity, ordering, and qualification, that are defined in the class diagram and sometimes further constrained by preconditions.

- Each postcondition in the contract must be achieved in the interaction diagram by a message that calls a basic command in the object that holds the responsibility.

- The control flow in a dynamic model begins at the instance of the façade controller that receives a message from the interface.

- When an object that is executing has no visibility to the object that must perform an operation, it should delegate the responsibility and the execution to another object that is closer to the one that holds the responsibility.

Santos (2007) presents a systematization of those principles by defining an automatic search-based production system capable of generating well-designed communication diagrams from a broad selection of contracts.

In addition to these principles, design patterns should be applied whenever possible to help the designer build methods that are effectively reusable and maintainable.

### 13.4.1 Creating instances — 13.4 Dynamic modeling based on postconditions

When a contract establishes that some instance was created, some other object must actually create it by sending a basic Create message in the respective sequence diagram. The Creator design pattern (Larman, 2004) states that the choice should be preferably:

- An instance of a class that has a composite or shared aggregation to the class of the object to be created.

- An instance of a class that has a one-to-many association to the class of the object to be created.

- An object that has the initialization data for the object to be created, and that is preferably associated to it.

**Figure 13–26: Conceptual model updated to be used as example in this chapter.** *(p. 268)*

> **Diagram content (transcribed from the figure image):** Design class diagram of SISMOB (refined conceptual model with ids/qualifiers): Controller qualified by id → Proposal (0..1, proposals) and → Person; Controller → */{ordered} proposals_by_deadline; Proposal {+status: ProposalStatus = waiting_changes; «imm» «unique» +id: ProposalId = Sismob.nextProposalId(); +name; «opt» +priority: Natural; +validity: Date = Date.today+Sismob.proposal_validity(); +/qualified_for_decision: Boolean}; Cancellation {+date: Date; +reason: String} 0..1 — 1 Proposal; Proposal * proposals_sent — 1 municipal_manager Person {+id: PersonId; +name; +email: Email}; Proposal 1 — {ordered}«stack» * Sending {date <= proposal.validity} {«imm» «unique» +id: SendingID = Sismob.next_sending_number(); «imm» +date: Date = Sismob.today(); «opt» +decision_motivation: MotivationText; «opt» +final_status: DecisionType}; Sending * sendings_received — 1 federal_manager Person; Sending qualified by id 1 — * assessments ProposalAssessment {«imm» «unique» +id: ProposalAssessmentId; +text: String; +opinion: String; +concluded: Boolean = False}; ProposalAssessment * assessments — 1 reviewer Person (qualified by id); Sending → Modification {+text}, FundsAllocation → FundsDeallocation, Publication, PhaseCompletionRequisition → PhaseAssessment; enumerations DecisionType {approved, cancelled, waiting_changes}, ProposalStatus {active, waiting_changes, concluded, cancelled}; «primitive» MotivationText {+text: String; +validate()}.

Each rule applies only if the previous one does not apply.

To serve as a reference for the following examples, let’s go back to our example of Sismob. Fig. 13–26 presents an updated version of the model where some qualifications were added and where we discovered that ProposalAssessment.concluded must not be derived but can have an initial value.

As a first example, let us work on the contract and dynamic model of an operation where a municipal manager creates an instance of Proposal that will not being sent yet.

The postconditions then would establish that an instance of Proposal is created, its status will be “waiting changes,” because it was not yet submitted. The id of the Proposal now is created by a service class called “Sismob.” The priority was discovered to be optional because it is the federal manager and not the municipal manager that defines it. The Proposal validity now is calculated automatically also using a function from a service class. The name of the proposal is received as argument by the system command.

After creating this instance, the link between the Controller and Proposal with role “proposals” must be created. Nothing to do with the link proposals_by_deadline because it is derived.

A link must be created between the person identified as the municipal manager and this proposal. And that is it. The OCL contract would be like:

```ocl
Context Controler::create_proposal(a_person_id, a_name)
    post:
        new_proposal.new_instance_of(Proposal) AND
        a_person[a_person_id]^add_proposals_sent(new_proposal) AND
        new_proposal^set_name(a_name) AND
        self^add_proposals(new_proposal)
```

Now let us see this same contract represented as a sequence of messages sent from one to another object. This is depicted in Fig. 13–27.

The sequence diagram used for dynamic modeling here has different kinds of messages:

- A message that invokes a system operation, which is sent by the interface and received by the controller: create_proposal, in the example.

- A basic query message that locates a specific person in the proposals role from the Controller to Person (get_person).

- A delegate message from Controller to the instance of Person (a_person) delegating the responsibility of creating and initializing a new Proposal.

- A basic command message from a_person that really creates the instance new_proposal (horizontal dashed arrow).

- Two more basic messages from a_person to new_proposal adding a_person as municipal manager and setting the name of the proposal to a_name.

- Finally, the controller sends to itself a basic command to add the new proposal to the role proposals.

Let us now see another example to emphasize the importance of using delegation to obtain low coupling in a project. We are going to specify the operation in which the municipal manager finishes its proposal and produces a Sending. In this case, a new instance of Sending should not be created by the Controler because there are no straight links from Controller to Sending. Proposal and Person are equally candidates to create a Sending. Having this equivalence, we simply chose Proposal to be the creator. It would be the case to consider a Proposal as a composite of Sending, although we decided not to officialize it. Considering a Sending as part of a Person would be nonintuitive.

Thus the context is: there is already a proposal linked to a municipal manager and we need to create a Sending, fill in its attributes, linking it to the proposal and linking it to a

**Figure 13–27: A sequence diagram that corresponds to the dynamic flow of the contract above.** *(p. 269)*

> **Diagram content (transcribed from the figure image):** Dynamic model for create_proposal: :Interface → :Controller create_proposal(a_person_id, a_name); Controller self-call a_person = get_person(a_person_id); Controller → a_person : Person new_proposal = create_proposal(a_person, a_name); Person creates new_proposal : Proposal; Person → new_proposal add_municipal_manager(a_person); set_name(a_name); Controller self-call add_proposals(new_proposal).

Person as a federal manager because it is a mandatory link from the Sending. First let us see the contract:

```ocl
Context Controller::send_proposal(a_proposal_id:ProposalId,
                                  a_federal_manager_id:PersonId)
    def:
        a_proposal = proposals[a_proposal_id]
        a_federal_manager = person[a_federal_manager_id]
    pre:
        a_proposal->notEmpty() AND
        a_federal_manager->notEmpty()
    post:
        new_sending.new_instance_of(Sending) AND
        a_proposal^add_sending(new_sending) AND
        new_sending^add_federal_manager(a_federal_manager)
```

In this contract, only a new instance and its two links are created. The Sending attributes are all with initial values or optional and thus do not need to be initialized during creation.

Now, for the dynamic model of this contract, we must remember that as the controller does not have association to Sending, it must delegate this creation, and it will be done by Proposal. In Fig. 13–28 first, the controller identifies the proposal and the federal manager by their ids. Then, a delegate message is sent to the proposal, with the federal manager as argument. The proposal then creates a new_sending, adds it to its role sending, and adds the federal manager to the new sending.

Now let us consider what happened if we do not follow the Do not speak to strangers design pattern. In Fig. 13–29, we allowed the controller to create the sending.

What happens here are two problems: first, a new visibility line that did not exist before was created between Controller and Sending. This increases the coupling of the system, which should be maintained low for a better organization of the code. Second problem is that the Controller is doing everything; the other objects are only arguments passed from one side to the other, but none of them has any proper behavior. This concentrates the processing and is as bad for object-oriented programming than spaghetti code is for structured programming.

**Figure 13–28: A sequence diagram with a delegate message.** *(p. 270)*

> **Diagram content (transcribed from the figure image):** send_proposal (delegated version): :Interface → :Controller send_proposal(a_proposal_id, a_federal_manager_id); Controller: a_proposal = get_proposals(a_proposal_id); a_federal_manager = get_person(a_federal_manager_id); Controller → a_proposal create_new_sending(a_federal_manager); Proposal: new_sending = Create() → new_sending : Sending; Proposal self add_sending(new_sending); Proposal → new_sending add_federal_manager(a_federal_manager).

**Figure 13–29: Violating the Do not speak to strangers pattern.** *(p. 271)*

> **Diagram content (transcribed from the figure image):** send_proposal (centralized in the controller): Controller gets a_proposal and a_federal_manager, creates new_sending : Sending, then calls new_sending.add_proposal(a_proposal) and add_federal_manager(a_federal_manager).

### 13.4.2 Destroying instances — 13.4 Dynamic modeling based on postconditions

The destruction of an instance is dynamically modeled by sending a destroy basic message to an object. The same principles of the creator design pattern apply here: the object that destroys an instance must have a shared or composite aggregation relationship with the object that is supposed to be destroyed, or an association from one to many, or, at least, be associated to the object.

Care must be taken to avoid leaving objects with mandatory links inconsistent after an object is destroyed. If the contract is well formed no orphan objects will be left, and the sequence diagrams only need to represent the postconditions that are mentioned in the contract.

As an example, let us present a situation where a reviewer can remove/destroy a proposal assessment of her authorship. The condition to the removal is that the proposal assessment is not concluded yet, accordingly to the attribute concluded.

```ocl
Context Controller::remove_proposal_assessment(a_reviewer_id,
                    a_proposal_assessment_id)
    def:
        a_reviewer = person[a_reviewer_id]
        a_proposal_assessment = a_reviewer.assessments[a_proposal_assessment_id]
    pre:
        a_reviewer->notEmpty() AND
        a_proposal_assessment->notEmpty() AND
        a_proposal_assessment.concluded = False
    post:
        a_proposal_assessment^destroy()
```

This contract assumes that the person who is the reviewer exists, and that the proposal identified exists also and is not concluded. Fig. 13–30 shows the sequence diagram that implements this contract. In this diagram, the one responsible to destroy the proposal assessment is the reviewer that created it.

**Figure 13–30: A sequence diagram for destroying and object.** *(p. 272)*

> **Diagram content (transcribed from the figure image):** remove_proposal_assessment: :Interface → :Controller remove_proposal_assessment(a_person_id, a_proposal_assessment_id); Controller: a_reviewer = get_person(a_reviewer_id); Controller → a_reviewer : Person remove_assessment(a_proposal_assessment_id); Person self: a_proposal_assessment = get_assessments(a_proposal_assessment_id); Person → a_proposal_assessment destroy() (object destroyed, ×).

Observe that the message remove_assessment between the Controller and a_reviewer is a delegate message. There is also a mark that ends the line of life of the proposal assessment just after it receives the message destroy().

### 13.4.3 Adding, removing, and replacing links — 13.4 Dynamic modeling based on postconditions

Our Sismob example, up to this point, does not have any operation that just creates a link between two existing objects. Every link is created just after a new object is created too.

Examples of links being created can be seen in Fig. 13–28 in the case of the operations add_sending and add_federal_manager, which are both basic commands to create links.

Methods to add links may be implemented usually in any of the participant classes. If the association is unidirectional, they should be implemented in the origin.

The same happens in the case of removing or replacing a link: add_role, remove_role, or replace_role.

The object that sends the message to create a link may be one of the participants of the link as in the case of add_sending sent by a_proposal to itself in Fig. 13–28. But it can also happen that the message that adds a link is sent by an object that does not participate in the link, such as in the case of the message add_federal_manager. In this case, the message should be sent to one of the participants of the link, and it should send the other participant as a parameter.

### 13.4.4 Modifying attributes — 13.4 Dynamic modeling based on postconditions

Another kind of postcondition that must be considered in dynamic modeling is the attribute value modification, which may be achieved by the basic setter message that can be sent by the object that owns the attribute or by one of its neighbors.

In the Sismob example, we could work with a command that changes the concluded attribute from a ProposalAssessment to True. The contract would be like this:

```ocl
Context Controller::conclude_assessment(a_person_id, a_proposal_assessment_id)
    def:
        a_person = person[a_person_id]
        a_proposal_assessment = a_person.assessments[a_proposal_assessment_id]
    pre:
        a_person->notEmpty() AND
        a_proposal_assessment->notEmpty() AND
        a_proposal_assessment.concluded = False
    post:
        a_proposal_assessment^set_concluded(True)
```

The sequence diagram for implementing this contract is shown in Fig. 13–31.

### 13.4.5 Conditional postconditions — 13.4 Dynamic modeling based on postconditions

As explained before, sometimes a postcondition must be obtained only if some given conditions are valid. In these cases, it is possible to use conditional messages in interaction diagrams that are similar to the guard conditions used in machine state and activity diagrams.

As an example, let us consider that a ProposalAssessment can only change the attributes text, opinion, and concluded if the attribute concluded is False. The contract for this operation is similar to the contract of a CRUDL update command, but the difference is in the fact that the postconditions can only be achieved if anther condition is True. The contract can be like this:

```ocl
Context Controller::update_proposal_assessment(a_person_id,
                    a_proposal_assessment_id,
                    a_text, an_opinion, is_concluded)
    def:
        a_person = person[a_person_id]
        a_proposal_assessment = a_person.assessments[a_proposal_assessent_id]
    pre:
        a_person->notEmpty() AND
        a_proposal_assessment->notEmpty()
    post:
        if a_proposal_assessment.concluded then
            Exception.raise(123)
        else
            a_proposal_assessment^set_text(a_text) AND
            a_proposal_assessment^set_opinion(a_opinion) AND
            a_proposal_assessment^set_concluded(is_concluded)
        endIf
```

**Figure 13–31: A sequence diagram where a value of an attribute is changed.** *(p. 273)*

> **Diagram content (transcribed from the figure image):** conclude_assessment: :Interface → :Controller conclude_assessment(a_person_id, a_proposal_assessment_id); Controller → person[a_person_id] : Person conclude_assessment(a_proposal_assessment_id); Person → assessments[a_proposal_assessment_id] : ProposalAssessment set_concluded(True).

Following our previous definitions, the postconditions in this case are conditioned. There are two cases do be dealt with: “assessment concluded” that produces to an exception and “assessment not concluded” that leads to its update with the parameters received.

The diagram of Fig. 13–32 in this case would need to use an alt fragment to deal with the two exclusive options.

Notice that the message sent from the controller to the person is a delegate one. It has the same name of the system command sent from the interface, because it has the same purpose. Then, the instance of person that has visibility to proposal assessments will coordinate the basic commands and queries necessary to do the job.

### 13.4.6 Exceptions — 13.4 Dynamic modeling based on postconditions

Sometimes preconditions cannot be converted to exceptions. Then they must be tested by the operation itself. UML unfortunately does not have a notation specific for dealing with exceptions in sequence diagrams. After seeing some proposals in literature and evaluating their complexity, we propose one that seems to be the most simple to draw. First, let us define a contract with exceptions, a contract to delete a Person that can only be completed if this person is not associated to proposal assessments, sendings_received, or proposals_sent:

```ocl
Context Controller delete_person(a_person_id)
    def:
        a_person = person[a_person_id]
    post:
        a_person^destroy()
    exception:
        a_person.assessment->notEmpty() IMPLIES Exception .throw(491)
        a_person.sendings_received->notEmpty IMPLIES Exception.throw(492)
        a_person.proposals_sent->notEmpty IMPLIES Exception.throw(493)
```

**Figure 13–32: A sequence diagram with an alt fragment.** *(p. 274)*

> **Diagram content (transcribed from the figure image):** update_proposal_assessment with exception: :Interface → :Controller update_proposal_assessment(a_person_id, a_proposal_assessment_id, a_text, a_opinion, is_concluded); Controller → person[a_person_id] : Person (same call); Person → assessments[a_proposal_assessment_id] : ProposalAssessment concluded = get_concluded(); alt [concluded = True] → raise(123) to :Exception; else → set_text(a_text), set_opinion(a_opinion), set_concluded(is_concluded).

Our proposal to deal with that is to put the postconditions into the first shape of the fragment alt defining as condition “[try].” Then, the other shapes of the alt fragment could be used to indicate the exceptions that can occur. Fig. 13–33 shows the appearance of this sequence diagram.

In this diagram, we replace the opt fragment in the case of the exception by guard conditions, that is, conditions that go between “[” and “].” This makes the diagram easier to read.

### 13.4.7 Postconditions over collections — 13.4 Dynamic modeling based on postconditions

When system commands have contracts with postconditions that specify updates over collections of objects, the iteration structure may be used in the communication diagram to indicate that a message is iteratively sent to every element in the collection. For example, the following system command increases the validity of every proposal within a deadline given by a number of days:

```ocl
Context Controller::extend_validity(a_number_of_days)
    post:
        proposals_by_deadline->forAll(
            ^set_validity(validity@pre+a_number_of_days)
        )
```

 )

In this case, a message set_validity will be sent to a set of objects iteratively. The respective sequence diagram could be like the one in Fig. 13–34.

**Figure 13–33: a sequence diagram that deals with exceptions.** *(p. 275)*

> **Diagram content (transcribed from the figure image):** delete_person with exceptions: :Interface → :Controller delete_person(an_id); alt [try] Controller → person[an_id] : Person destroy(); exception branch: [get_assessment()->notEmpty] throw(491); [get_sendings_recieved()->notEmpty] throw(492); [get_proposals_sent()->notEmpty] throw(493) to :Exception.

**Figure 13–34: A sequence diagram that updates a collection of objects.** *(p. 276)*

> **Diagram content (transcribed from the figure image):** extend_validity: :Interface → :Controller extend_validity(a_number_of_days); loop [for all] Controller → proposals_by_deadline : OrderedSet<Proposal> set_validity(validity@pre + a_number_of_days).

## 13.5 Delegation and low coupling

*Chapter 13 · p. 276*

Up to this point, we have seen some techniques for building sequence diagrams. But in most situations, there is more than one design option and more than one way to send a message.

As discussed earlier, sometimes the object that has control does not have visibility to the object that can perform the responsibility. In this case, two opposite design approaches can be identified:

- The object that has control tries to obtain a reference to the object that can perform the responsibility and communicate directly with it.

- The object delegates the message to another object that is closer to the object that can perform the responsibility.

To understand the difference between these two approaches, imagine that Mary is the boss of Peter. The boss wants to order a buffet for the office party, but she does not know any catering companies. The boss knows that Peter has contact with some catering companies, and then, two approaches are possible:

- The boss asks Peter for the phone numbers of the companies and makes the arrangements herself. The only thing that Peter does is to pass his contacts to the boss.

- The boss sends Peter the parameters for the party: how many people, what kind of food, how much to spend, etc., and asks Peter to do the arrangements. The party happens, and the boss delegated the most part of the work to Peter.

Although in real life, it may be interesting to contact many people and companies, this is not the case in object-oriented systems. When objects are highly coupled, the system is more complex than it really needs to be. Thus it is necessary to avoid creating connections between objects that were not connected in the first place.

The first approach discussed just above is called concentration. With it the object that has execution control manages to obtain references to all objects needed and performs the operation itself. The second approach is called delegation, and it consists of making the objects delegate responsibilities when they cannot perform those themselves. The second approach is usually preferable, because it provides more potential for reusing classes and methods, because the intermediary queries or delegated methods that this approach creates usually are reusable.

Let us repay attention to a contract shown before, in which a user, a municipal manager, sends a proposal to the system after having registered it.

```ocl
Context Controller::send_proposal(a_proposal_id:ProposalId,
                                  a_federal_manager_id:PersonId)
    def:
        a_proposal = all_proposals[a_proposal_id]
        a_federal_manager = person[a_federal_manager_id]
    pre:
        a_proposal->notEmpty() AND
        a_federal_manager->notEmpty()
    post:
        new_sending.new_instance_of(Sending) AND
        a_proposal^add_sending(new_sending) AND
        new_sending^add_federal_manager(a_federal_manager)
```

We can recall that the diagram in Fig. 13–28 shows a possible implementation for this contract that does not increase the number of links between objects because it uses only the association links already present.

With the concentration approach, the whole process would be implemented in the Controller class. As seen in Fig. 13–29, this class would obtain all necessary data to perform the system command. In the concentration sequence diagram, all the messages are sent by the Controller. No delegation happens, as no object sends messages and the Controller instance acquires visibility to all objects that it interacts with.

Both approaches solve the problem. But by using the delegation approach, the query can be implemented with more cohesion and less coupling.

Fig. 13–35 shows the flow of messages between objects and therefore the dependencies that must exist between classes.

In the concentration diagram, a new link between the controller and an instance of Sending is created although a path from Controller to Sending already exists through Proposal and also through Person.

The price for using delegation is usually having more methods declared in the intermediary classes. However, reusable methods are usually produced to counteract this issue. The price for using the concentration approach is having a design where responsibilities are concentrated in the façade controller instead of being distributed among the objects; this produces a model that is hard to evolve and maintain in the long term.

## 13.6 Design class diagram

*Chapter 13 · p. 277*

One of the goals of the logical design is to build and refine the DCD, which is created from the conceptual model and from information obtained during dynamic modeling (when the interaction diagrams for the contracts are being built).

**Figure 13–35: Dynamics of message sending between instances of classes with the delegation and the concentration approaches.** *(p. 278)*

> **Diagram content (transcribed from the figure image):** Two design styles for creating a link. Delegation: Controller → Proposal → Sending, and Controller → Person; the Person—Sending link already exists and the work is delegated along existing links. Concentration: Controller directly links to Proposal, Sending (new link created) and Person; the existing links Proposal—Sending and Person—Sending are reused.

The first version of the DCD is an exact copy of the conceptual model, which will be modified later. The basic modifications that are made in the DCD during domain tier design are the following:

- Methods are added. During analysis, only system commands and queries were discovered and added to the façade controller class. During design, delegate and basic methods belonging to other classes are added.

- Associations are directed. During analysis, associations were nondirectional. During design, their direction is determined by the direction of the messages flowing between objects in the interaction diagrams.

- Attributes and associations may be detailed. It is not mandatory to present details about attributes and associations during analysis. These details may be added during design. Additionally, in analysis, only abstract data types are used to specify association roles, and they may be replaced by concrete data types during design (e.g., replacing sequence by array list or linked list).

- The structure of classes and associations may change. It may be necessary to create new classes to implement certain design structures, such as strategies and services, for example. Thus it is possible that the class structure of the DCD does not correspond exactly to the structure of the conceptual model, in some cases.

- Possible creation of protected and private attributes. In the conceptual model, all attributes are public because they represent static information and not behavior. However, when

the dynamic aspects of objects are represented, it may be necessary to work with private attributes to encapsulate internal states that determine the behavior of some objects. These attributes sometimes may not be directly accessible through a getter or setter, but their influence on some methods is felt.

During the construction of a communication diagram, each time an object receives a delegated message, its class must implement the corresponding method.

The DCD may also include information about the direction of the associations if the designer chooses not to implement every association as bidirectional. This is usually the case because unidirectional associations tend to be simpler to implement and more efficient when compared to bidirectional associations.

Deciding whether an association is unidirectional or bidirectional depends on the flow of messages on the interaction diagrams. No association should be, in principle, navigable in the direction of the controller: the controller sees the classes, but they do not see it. Other associations may be unidirectional if the messages only flow in one direction, and bidirectional if messages flow in different directions, even if that happens in different sequence diagrams.

Associations that links were not used by messages are left undefined (nondirectional) until another diagram eventually decides on their direction.

If other sequence diagrams developed for different system operations require messages navigating in the opposite direction as those that were already discovered, then the respective associations should be bidirectional.

The logical design activity finishes when the DCD has enough information to implement the domain tier classes. That usually happens when all system operation contracts have been examined and their dynamic models incorporated into the design.

## Questions (Chapter 13)

1. What are the six kinds of responsibilities that objects may have? What kind of method is used to perform each responsibility?

2. What are the four kinds of visibility that may exist between objects? Are they symmetrical? How does each of them influence high coupling among classes?

3. Explain the influence of contract preconditions and exceptions in dynamic models. How do they affect the complexity of the dynamic model?

This page intentionally left blank

