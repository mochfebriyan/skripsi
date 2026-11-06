<!-- Knowledge file: Chapter 7 — System operations -->
> **About this file.** Chapter 7 of a cleaned, AI-ready edition of Wazlawick, R. S. (2024). Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-443-13739-6.  
> **Covers:** System sequence diagrams with actor, interface and controller; system events vs system commands and queries; stateful vs stateless; alternate flows in SSDs.  
> **Use this file when:** drawing system sequence diagrams from use cases or identifying system operations.  
> **Sections:** 7.1 Introduction to system operations (p. 107); 7.2 Elements of a sequence diagram (p. 110); 7.3 Expanded use cases as system sequence diagrams (p. 112); 7.4 Connecting the interface to the façade controller (p. 114); 7.5 Stateful and stateless (p. 116); 7.6 Alternate flows in system sequence diagrams (p. 117); 7.7 Discussion (p. 118)  
> **Contains:** 8 figures transcribed as text, 0 code listings.

# Chapter 7: System operations

*Source: Wazlawick, Object-Oriented Analysis and Design for Information Systems, 2nd ed. (Elsevier, 2024), starts p. 107*

Key topics in this chapter

- System events

- System returns

- System commands

- System queries

- Sequence diagrams

- Stateless and stateful

## 7.1 Introduction to system operations

*Chapter 7 · p. 107*

Among other uses, the text of the detailed use cases may be used as:

- A source of information to discover the concepts and attributes for refining the conceptual model.

- A source of information to discover system operations, which are the operations that encapsulate the domain tier of the system from its interface.

There are two kinds of system operations:

- System commands, which change data and must not return data.

- System queries, which return data and must not change data.

That follows the Command-Query Separation or CQS principle of software engineering (Meyer, 1988), which aims for better code reusability and maintainability. A query that changes data would be less cohesive than a query without collateral effect and a command without return.

System commands are methods that may be activated by a system event, that is, as a reaction to a user action. System commands, by definition, implement a flow of information from the outside to the inside of the system (input). Therefore system commands update the information that is managed by the system, usually in databases.

System queries are methods that correspond to the simple verification of information already stored. That information may be presented exactly as it is stored or modified by logical and mathematical operations. By definition, a system query may not be responsible for the insertion of new information into the system (that would be a side effect, a kind of antipattern). It should also not be responsible for updating or removing information from the system: it can only read information. 

109

The set of system operations corresponds to the whole functionality of a system, that is, the set of all functions that can be performed by a user with the system.

Use cases are excellent sources for discovering system operations. System commands are basically associated to steps in which the user sends some information to the system (inputs). System queries are associated to use case steps in which the system sends information to actors (output).

## 7.2 Elements of a sequence diagram

*Chapter 7 · p. 110*

One of the UML diagrams that can be particularly useful for representing the sequence of system events and returns in a use case is the sequence diagram. When a sequence diagram is used to represent a use case, it may be called a system sequence diagram (Larman, 2004). The system sequence diagram has elements that are instances of actors and other system components (expressions preceded by “:,” as e.g.,:User,:Interface). In the first version of the system sequence diagram, only the actors and the system interface (or application tier) are represented (Fig. 7–1).

The activities related to use case analysis still do not deal with objects that are internal to the system. Thus the system must be represented as a single object: a black box. In this case, it can be represented by the interface symbol, as proposed by Jacobson et al. (1992) and seen in Fig. 7–1 (right side). One actor can only communicate with a system through its interface. Messages from the actor cannot reach directly any internal object, as shown in Fig. 7–2.

**Figure 7–1: Information flows from/to users and interface.** *(p. 110)*

> **Diagram content (transcribed from the figure image):** Sequence diagram with lifelines :Actor 1, :Actor 2 and boundary object :Interface; messages labelled "information" flow from actors to the interface and back (Actor 1 → Interface, Interface → Actor 1, Actor 1 → Interface, Interface → Actor 2, Actor 2 → Interface, Interface → Actor 2) — actors exchange information only through the interface.

**Figure 7–2: Example of antipattern where interface communicate with object surpassing the interface.** *(p. 111)*

> **Diagram content (transcribed from the figure image):** Sequence diagram rule. Lifelines :Actor, :Interface, :User, :Project. CORRECT: the actor exchanges messages only with :Interface. WRONG: the actor sends messages directly to internal objects :User and :Project ("the actors cannot communicate directly with any internal object").

Actors, interfaces, and other elements of the sequence diagram have a lifeline, represented by a vertical line, where events may happen. When the line is dashed, the element is inactive. When the line is solid, the element is active (processing or waiting for the result of an operation being performed by another element). Human actors are always considered active.

The horizontal arrows represent the information flow. There are three kinds of information flows in this diagram:

- Between actors: Actors’ communication among themselves without using the system, corresponding maybe to complementary steps of the expanded use case.

- From the actors to the system: Corresponding to system events, that is, steps that correspond to the inputs of the expanded use cases.

- From the system to the actors: Corresponding to system returns, that is, steps that correspond to the outputs of the expanded use cases.

The information exchange between actors does not belong to the scope of the system, but it may be useful to illustrate how information is exchanged from actor to actor until reaching the system, if necessary.

One thing to keep in mind when these diagrams are being built is that information usually does not appear from nothing; it must be transferred from actors to system and vice versa. The actor usually has some information that must be passed to the system to perform a process. A reviewer that wants to save and assessment should inform the system who she is, which project is being assessed, and what is the text of the assessment. In the beginning of this use case, the reviewer is the only one who holds all that information; the system has the registry of all projects and reviewers, but it cannot know who is going assess that specific project until someone provides that information.

The sequence diagram can be built for the main flow of a use case and completed with some or all alternate flows if necessary.

The most important thing at the moment is to discover what information is being exchanged between the actors and the system. The analyst must build a catalog with all system operations (which are explained in the next sections) discovered in the main and alternate flows of the use case. This information will be used later to define contracts that indicate how the system retrieves and transforms information.

## 7.3 Expanded use cases as system sequence diagrams

*Chapter 7 · p. 112*

The system sequence diagram is a tool for achieving more formal and detailed use case descriptions. Additionally, developing the system sequence diagram makes the connection between requirements analysis (the expanded use case) and software design (the system operations that will be implemented).

The construction of the system sequence diagram may be done in two stages:

1. Representing the steps of the use case as information exchange between actors and the system interface.

2. Representing system operations as operations calling between the interface and the façade controller,^1 which encapsulates the domain tier of the system.

The first step is simple: for each use case input, there is an equivalent system event in which one actor sends information to the interface, and for each use case output, there is an equivalent system return in which an actor receives information from the system (Fig. 7–3).

Note that between actors and interface, the flows consist of sending and receiving uniquely information. Information may be sent by an actor, for example, by typing it in a form. Information can be received by an actor when it is printed on the screen. At this level, flows are not calling operations because actors usually are not computers.

The words or expressions used to represent information are sometimes a source of confusion and misunderstanding. To avoid such confusion, a writing pattern is suggested:

- Simple information (alphanumeric data) is represented by one or more words. For example, name, assessment, and project number.

- Complex information may be represented between “ , ” and “ . ” in the diagram if it is composed by a few elements (two or three). For example, ,name, date of birth, address..

- Complex information composed of numerous elements (more than three) may be represented in a separate note or data dictionary. Only the name of the complex concept is used in the diagram. For example, the data dictionary could contain this definition: dto_project 5 , number, name, initial date, description, author, municipality, value . . In this case, when all this information must be passed in a sequence diagram, the word “dto_project” should be used instead.

> *Footnote 1:* A façade-controller provides “a unified interface to a set of interfaces in a subsystem. Façade defines a higherlevel interface that makes the subsystem easier to use” (Gamma et al., 1995).

- A simple command that does not include alphanumeric information being passed may be represented between parentheses. For example, (search for project) or (confirm).

- A collection of values can be indicated by the suffix “– * .” For example, dto_project– * is a set of projects.

- When one object is selected from a collection presented by the system, the selection is indicated by the word “selected,” as in Fig. 7–4, where “selected project” stands for a project that was selected from the set dto_project– * presented by the system.

- The information contained in a dto_project is probably a subset of the attributes of the Project class of the conceptual model; it does not necessarily correspond to the complete set of attributes of the Project class, but only the ones the user needs for choosing a project.

**Figure 7–3: System event and system return.** *(p. 113)*

> **Diagram content (transcribed from the figure image):** Actor → Interface message "information" labelled Input: system event; Interface → Actor message "information" labelled Output: system return.

**Figure 7–4: Commands and information flowing between user and interface.** *(p. 113)*

> **Diagram content (transcribed from the figure image):** System sequence diagram for assessing a project (actor :Reviewer, :Interface): Reviewer → (search for project); Interface → Reviewer: dto_project* (list of projects); Reviewer → Interface: selected project.

- In the last step, when the user selects a project and informs the system which one it is, she does not have to send all the information contained in the respective dto_project. It only sends the project identification that usually should not even be known by the user. It is an information hidden to the user, that comes out as part of each dto_project, and is sent back to the system without explicit knowledge of the user. The user only knows that she has picked an option from a list.

## 7.4 Connecting the interface to the façade controller

*Chapter 7 · p. 114*

System events are actions that a user performs over the system interface. When a web interface is used, for example, these actions consist of filling forms, pressing buttons, etc. These are not operations in the sense of programming languages, that is, these flows from an actor to the system and vice versa should not be labeled with operations or methods calling (messages).

However, system commands and system queries are computational operations that are necessary to implement system events and system returns, respectively. System commands and queries are activated by messages that are sent from the interface to the façade controller. Now, we have a system component that invokes another system component. In this case, it is the interface that sends a message, asking the façade controller to perform a method that consists of a command or a query. The set of all possible messages is equivalent to the whole functionality of the system: all data access and updating are done by system commands and queries.

Thus four kinds of arrows are of interest in system sequence diagrams, and they are shown in Fig. 7–5:

- System event: this is an action performed by an actor that sends some information to the interface. It can be a single command, single information, a complex information (DTO), or a list of information and DTOs, recursively.

**Figure 7–5: Adding second level: system commands and queries.** *(p. 114)*

> **Diagram content (transcribed from the figure image):** Three-lifeline SSD :Actor, :Interface, :Controller. Actor → Interface: info_1, info_2, info_3 (system event); Interface → Controller: sys_command(info_1, info_2, info_3) (system command); Interface → Controller: dto_result = sys_query(info_1, info_2, info_3) (system query); Interface → Actor: dto_result (system return).

- System return: this is a flow of information from the interface to one or more actors. It usually consists of the same structures that are used with system events.

- System command: this is a message that is sent from the interface to the controller, usually in response to a system event. The system command must, by definition, change some information stored or managed by the system. In the diagram, this is represented by an arrow from the interface to the controller labeled with a message. The use of parentheses is always recommended to distinguish it from information flows, such as system events and returns. Thus even a message with no arguments should be represented here as message().

- System query: this is a message that is sent from the interface to the controller to obtain some information from the system. Queries must not change data; they just return data. In the diagram, queries are represented by arrows from the interface to the controller labeled with a message with an explicit return value. In the example, the return value is represented by dto_result.

The domain tier of an application (the part of the system that contains all classes that perform the logical operations on data) is encapsulated by its façade controller, which is an instance of a class that implements all system commands and queries that must be accessed by a given interface or set of interfaces.

There are at least three subpatterns for the façade controller. The first one, for smaller systems, consists of implementing a single controller for the whole system. However, this would result in many operations implemented in a single class.

A solution to this is to divide it into use case controllers, that is, a different controller class for each use case. However, this is not a good solution when different use cases call the same methods, which should be implemented in different classes.

The most adequate solution for most medium or large systems is to implement component or subsystem controllers, that is, controllers that encapsulate the functionality of subsystems or components as defined by the system architecture.

The design of messages between the interface and the controller is made after an examination of the system events and returns using the following rules:

- A system event that sends data that must be stored, updated, or deleted, that is, data that cause a change in the internal state of the system, require at least one system command to be defined. More than one command may result from a single system event too.

- A system return that sends data obtained from the controller requires at least one system query between the interface and the controller, so that the data can be obtained from the controller in order to be presented by the interface.

- A sequence of system event and return, where the event just provides arguments for producing the return, requires a system query (not a command) where the information received from the system event is composed only by its arguments (Fig. 7–6).

The cause/consequence relation between events and commands and between returns and queries is not always so straight. Sometimes, a query can use arguments that were passed to the interface many steps earlier, or information passed by the actor to the interface can be used many times by different system commands and queries.

**Figure 7–6: A query with arguments.** *(p. 116)*

> **Diagram content (transcribed from the figure image):** Stateless query pattern: Actor → Interface: arguments; Interface → Controller: dto_result = sys_query(arguments); Interface → Actor: dto_result.

## 7.5 Stateful and stateless

*Chapter 7 · p. 116*

When the system sequence diagram is being developed, each piece of information is passed from the actor to the interface just once. However, in the next level, between interface and controller, many different commands and queries may need the same arguments. For example, the customer ID may be necessary to perform many subsequent operations.

There is an antipattern named stateful that allows the controller to remember data sent by the interface even if these data are not registered in a permanent way. With the stateful pattern, the interface could send the ID just once, when the first operation is called, and maintain it in temporary memory so that the subsequent operations do not have to send the ID again.

This seems to be a good idea, because it avoids data being sent more than once between interface and controller. However, it has disadvantages. The main maybe is that it creates temporal dependence among operations. For example, the second operation needs the ID, but it is not sent by the interface because it was already sent for the first operation. In this case, the second operation has the ID as an implicit argument, which is stored someway in the controller memory. That problem is called temporal dependency. This is bad when we need to reuse operations in different contexts and thus must be avoided.

Instead, we should use the stateless strategy that assumes that the control does not have any temporary memory (does not have an internal state besides the database), and thus, each operation should receive every argument explicitly.

Fig. 7–7 shows how the system sequence diagram would look for the main flow of the use case “Update assessment” with a stateless strategy. The information is passed from the actor to the interface just once, but each time a system command or query needs that information, the interface should send it again as an argument to the controller. Observe that selected_project and user_ID are sent twice by different system operations.

Observe also that user_ID is known by the interface, it is not stored in the controller. That is why it is sent every time user identification is needed. Also, user_ID may be a complex information, not just a number. It may also be a hash number that codifies the user identification and password and can be extracted by the controller.

**Figure 7–7: A stateless system sequence diagram for the main flow of the use case “Update assessment.”** *(p. 117)*

> **Diagram content (transcribed from the figure image):** SSD for "assess project" with note PRECONDITION: reviewer is logged in and user_ID is known. Reviewer → Interface: (search for project); Interface → Controller: dto_project* = list_projects(); Interface → Reviewer: dto_project*; Reviewer → Interface: selected project; Interface → Controller: assessment = get_assessment(selected project, user_ID); Interface → Reviewer: assessment; Reviewer → Interface: updated_assessment; Interface → Controller: set_assessment(select project, user_ID, updated_assessment); Controller ⇢ Interface: success (dashed return); Interface → Reviewer: MSG.342 (confirmation message).

## 7.6 Alternate flows in system sequence diagrams

*Chapter 7 · p. 117*

As seen before, use case steps, especially system events, may have exceptions, which are handled by an alternate flow (variant or exception handler).

The insertion of those alternate flows in a system sequence diagram may be done in stages. Initially, the exceptions may be indicated in the diagram where they occur by using alt fragments.

* = Suppose that dto_project– is an empty list when the diagram in Fig. 7–7 is running. According to the requirements seen in Chart 6.1, it must show MSG.049. The user cannot proceed further. Her options are inserting a new project or quitting.

This is shown in Fig. 7–8 where a fragment alt is used. It works much like the if-then-else instruction in programming languages. If the condition [dto_project– * is empty] is true, then the first lane is executed (the one above the dashed line). Otherwise, the second lane is performed (the one below the dashed line).

In the first lane, there is also a fragment ref to indicate that another sequence diagram is executed at this point, in the case, SQ.39 insert assessment. The ref fragment works like a procedure call or a macro in programming languages. In the current example, there is no return and the use case simply ends after SQ.39 is executed.

As quitting is an option that is usually allowed at any point in the flow, it should not be represented in the diagram.

The same happens to other exceptions that can occur at any time. The UML sequence diagram has no explicit way to represent try-handle structures. But we could represent the exceptions, if needed, after the main flow as opt fragments stereotyped with “ ,, exception ...” The opt fragment should have only one lane and one condition, and it corresponds to an if-then structure, without the else.

**Figure 7–8: Adding fragments to represent exceptions.** *(p. 118)*

> **Diagram content (transcribed from the figure image):** Same SSD as Fig 7–7 with an alternate flow: after dto_project* = list_projects(), an "alt" fragment: [dto_project* is empty] → Interface → Reviewer: MSG.049 and a "ref" to SQ.39 insert assessment; else → main flow (dto_project*, selected project, get_assessment, assessment, updated_assessment, set_assessment, success, MSG.342).

Finally, when a variant makes the flow entering a loop, for example, a variant in step 5 sending control back to step 3, a loop fragment can be used. The loop works like a “while” structure in programming languages. It has a condition, and the flows inside it are repeated until this condition is false.

## 7.7 Discussion

*Chapter 7 · p. 118*

Perhaps, the main practical result of the system sequence diagram modeling is the discovery and design of the system commands and queries that must be implemented to allow the functionality of the system to be available for the users. As seen in Fig. 7–8, the following system queries must be implemented:

- list_projects():List of DTO

- get_assessment(a_project, a_user):Text

Besides, the following system command must also be implemented:

- set_assessment(a_project, a_user, a_text)

Some of those operations could be in the usual pattern operations such as: getter/setter, list, and get/add/remove/replace. In this case, they must not be further inspected. However, other operations outside known patters can be expanded further, as seen in next chapters.

## Questions (Chapter 7)

1. How are variants and exceptions modeled in a system sequence diagram?

2. Why is the stateless pattern preferable to stateful?

3. Which programming language structures are represented by the fragments: alt, opt, loop, and ref?

4. Can a simple system event send data to both a query and a command? Give an example.

5. Does every step in a real use case correspond to a system query or command?

This page intentionally left blank

