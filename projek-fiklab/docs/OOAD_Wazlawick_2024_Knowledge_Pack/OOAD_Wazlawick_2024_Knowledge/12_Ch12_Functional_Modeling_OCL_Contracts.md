<!-- Knowledge file: Chapter 12 — Functional modeling with object constraint language contracts -->
> **About this file.** Chapter 12 of a cleaned, AI-ready edition of Wazlawick, R. S. (2024). Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-443-13739-6.  
> **Covers:** Functional modeling with OCL contracts: preconditions, exceptions, postconditions for system commands and queries, return values, examples.  
> **Use this file when:** specifying the behaviour of system operations precisely (pre/postconditions, business-rule exceptions).  
> **Sections:** 12.1 Introduction to functional modeling (p. 216); 12.2 Preconditions (p. 220); 12.3 Exceptions (p. 224); 12.4 Preconditions and exceptions versus invariants (p. 226); 12.5 Query return (p. 227); 12.6 Postconditions (p. 228); 12.7 Pattern contracts for CRUDL (p. 241); 12.8 Discussion (p. 246)  
> **Contains:** 7 figures transcribed as text, 43 code listings.

# Chapter 12: Functional modeling with object constraint language contracts

*Source: Wazlawick, Object-Oriented Analysis and Design for Information Systems, 2nd ed. (Elsevier, 2024), starts p. 216*

## Key topics in this chapter (Chapter 12)

- Preconditions

- Postconditions

- Query returns

- Exceptions

- System Operation Contracts

## 12.1 Introduction to functional modeling

*Chapter 12 · p. 216*

Before functional modeling begins, the analysis process may have already produced two artifacts:

- The refined conceptual model, which represents statically the information managed by the system.

- The expanded use cases or system sequence diagrams, which show how potential users exchange information with the system, without mentioning how that information is processed internally by the system and in some cases even without mentioning the interface technology.

When system sequence diagrams are built, the system commands and queries that must be implemented are identified. Each system command and query imply a user intention or goal; for example, the reviewer may be providing information on which proposal she is going to asses, or she may be looking for the list of assessments she has done in the last 30 days. That intention is captured by system command contracts and system query contracts, generically referred to as system operation contracts, which corresponds to the functional model of the system.

A system command contract may have three sections:

- Preconditions (optional): Logic statements that are assumed to be true by the command and therefore should not be checked by it. For example, “all assessments in the list are completed.”

- Postconditions (mandatory): Logic statements that explain how the command changes existing information if it is successfully executed. For example, “one assessment was created and associated to the proposal and reviewer.”

- Exceptions (optional): Logic statements that contain conditions that could prevent the command from succeeding, and that will be checked by it. For example, “the deadline for the assessment is past.” 

217

On the other hand, a system query contract may have the following sections:

- Preconditions (optional): Logic statements that explain what is assumed to be true by the query and therefore should not be checked by it. For example, “The assessment list is not empty.”

- Results (mandatory): A data structure that defines the information that the query returns. For example, “a list with all reviewers sorted by seniority.”

- Exceptions (optional): Logical conditions that were added by the designer to prevent the system from performing the query in some situations. For example, “the user has no authorization to change this record.”

Preconditions exist in both types of contracts. They define constraints that are complementary to the ones already existing in the conceptual model. Preconditions are assumed to be true by the operation. This means that preconditions are not tested by the operation that is defined by the contract; they must be tested and assured before the operation is performed.

Postconditions, on the other hand, exist only in system command contracts because they specify how the information kept by the system was changed. Special care must be taken to not confuse postconditions with query results. By the Command-Query Separation principle (Meyer, 1988), it is not appropriate for a command to return any result (except in special justified cases). Queries, on the other hand, must return some result, but cannot produce any change in the existing information. Therefore system queries must have results and system commands must have postconditions usually.

As opposed to preconditions that must be true before the operation is called, exceptions are situations that usually cannot or should not be tested before; exceptions are tested by the operation itself. Exceptions are events that, if they occur, prevent the operation from succeeding.

Exceptions in command contracts and exceptions in query contracts may have distinct purposes. In command contracts, exceptions are used when arguments or existing information does not satisfy a given business rule (e.g., trying to register a customer that is already registered).

However, in query contracts, exceptions have a different meaning. As a query does not change information, there is no invalid argument that could possibly prevent a well-defined query from being performed. If a user queries a system about a person that does not exist, the query is not prevented from being performed: it would answer that there is no person for the query; this is the right answer, not an exception.

Exceptions in queries would be used only if by any chance the team decides that for a given condition, the query must not be performed. Usually, those conditions are related to security issues, or other technological concerns such as multiwindow interface, concurrency, and communication. As these issues are usually not addressed by functional modeling, exceptions in queries contracts are not frequent at this point.

Normally, in an operation contract, be it a command or query, an exception can be transformed into a precondition and vice versa. The decision on designing an issue as a precondition or exception determines which part of the system is responsible for testing that issue: the calling operation or the called operation. Usually, in large multiuser systems, concurrent race conditions^1 may lead to choosing to avoid preconditions; however, if the system is not subject to complex concurrency or a concurrency control mechanism that prevents data from changing during transactions exists, then a design based on preconditions may be the better choice.

**Figure 12–1: Conceptual model to be used in examples.** *(p. 219)*

> **Diagram content (transcribed from the figure image):** Conceptual model used for contracts (SISMOB): Controller (one-way) → * Person and →(qualified, 0..1) */{ordered} proposals_by_deadline Proposal {«imm» «unique» +id: ProposalId; +name; +status: ProposalStatus; +priority: Natural; +validity: Date; +/qualified_for_decision: Boolean}; Proposal * proposals_sent — 1 municipal_manager Person {+id: PersonId; +name: String; +email: Email}; Proposal 1 — {ordered}«stack» * Sending {date <= proposal.validity} {«imm» «unique» +id: SendingID; «imm» +date: Date = Sismob.today(); «opt» +decision_motivation: MotivationText; «opt» +final_status: DecisionType}; Sending * sendings_received — 1 federal_manager Person; Sending 1 — * assessments ProposalAssessment {+text: String; +opinion: String; +/concluded: Boolean = sending->notEmpty()}; ProposalAssessment * assessments — 1 reviewer Person; Sending 1 — * Modification {+text}; Sending 1 — 0..1 FundsAllocation → FundsDeallocation, Publication, PhaseCompletionRequisition → PhaseAssessment; Cancellation 0..1 — 1 Proposal; enumerations DecisionType {approved, cancelled, waiting_changes}, ProposalStatus {?}; «primitive» MotivationText.

For the examples in this chapter, a partial refinement of the conceptual model presented in Fig. 10–4 will be used, now represented as Fig. 12–1.

Also, we will be using the sequence diagram of Fig. 7–7, now represented as Fig. 10–2 to identify the system operations that are necessary for this use case. A few modifications were done to reflect new knowledge about the project. For example, what are being searched in this use case are not projects, but their sendings. Also, when a reviewer looks for an assessment, she wants to know only her assessments, not everyone’s. That is while the argument user_id was added to the list_sendings query.

As a precondition for this sequence diagram, we see that user_id is known because it is guaranteed that the user logged in before this use case started.

The system operations we are looking for are in the space between the interface and the controller. As we are using the stateless strategy, the operations would look like:

- list_sendings(user_id):OrderedSet , DTO_Sending.. In this case, remember that DTO_Sending is a list of alphanumeric values defined in the data dictionary of the project and the return of the query is defined as an OrderedSet, which could be sorted by different criteria on the interface. It is not a regular Set because it would need to be converted before sorting, and it is not also a Sequence because there is no need to repeat objects in this list. The attribute user_id was added as an argument to avoid the user to receive sendings to which she is not associated with.

> *Footnote 1:* For example, after a user orders a product, while the user is closing the order and providing payment, the only available product could be sold to another user. This must be avoided with concurrency control mechanisms.

- get_assessment(selected_sending, user_id):Text. This query returns the existing text of an unfinished assessment or the empty string if none is available.

- set_assessment(selected_sending, user_id, updated_assessment). This is the only system command in this use case, which updates the text of the verified assessment by the reviewer. Although a sending may have multiple assessments, they must all be from different reviewers. An invariant should be written to guarantee that (consider it as an exercise).

In the next sections, we will be presenting the components of a system operation contract: preconditions, returns, postconditions, and exceptions. The chapter finished with the presentation of standard CRUDL contracts.

## 12.2 Preconditions

*Chapter 12 · p. 220*

Preconditions establish what must be true when a system query or command is performed. For example, for every operation in Fig. 12–2, there is a preliminary precondition that states that the user is logged in and that her id is user_id.

Thus the three operations in that diagram could establish that this fact did not change until they are performed by declaring the same precondition in the definition of their functionality. Observe that all three operations are implemented in the class Controller and that they are being called by the interface. Thus Controller will always be the context for system operations. This is the precondition for list_sendings:

```ocl
Context Controller::list_sendings(user_id:UserId):OrderedSet<DTO_sending>
    pre:
        self.person->exists(a_person|
            a_person.id = user_id
        )
```

)

**Figure 12–2: A system sequence diagram used in some examples in this chapter.** *(p. 220)*

> **Diagram content (transcribed from the figure image):** Numbered SSD for assessing a proposal (PRECONDITION: reviewer is logged in and user_id is known): 1: (search for proposal); 1.1: sending* = list_sendings(user_id); 1.2: dto_sending*; 2: selected_sending; 2.1: assessment = get_assessment(selected_sending, user_id); 2.2: assessment; 3: updated_assessment; 3.1: set_assessment(selected_sending, user_id, updated_assessment); 3.2: success (return); 3.3: MSG.342.

Abbreviated form:

```ocl
Context Controller::list_sendings(user_id)
    pre:
        person->exists(
            id = user_id
        )
```

The precondition would be the same for the other two operations as they both receive user_id as argument.

Looking closely to the precondition, it becomes true if exists at least one person with a given id. It could be the case that many persons could exist with the same id. However, as the id attribute of Person is unique, that cannot be the case. Only one instance of Person can have the given id.

To be useful for software development, preconditions must be expressed in a careful way. They must reflect facts that can be identified in the previously developed conceptual model, or the model must be updated to reflect the new information just discovered. This justifies the use of formal languages such as object constraint language (OCL) for writing contracts (Warmer and Keppe, 1998) instead of natural language.

Preconditions may be classified into two groups:

- Parameter guarantee: Preconditions that assure that the arguments of a command or query correspond to valid objects (e.g., “there exists a person with the id passed as an argument”).

- Complementary constraint: Preconditions that further constrain the conceptual model when performing a given command or query, to assure that the information is in a given state when the operation is being executed. For example, in a context where an instance of Sending can be associated with zero or more assessments, a precondition such as “the sending has received no assessment” is a complementary constraint that reduces the possibilities from zero or more to zero only.

### 12.2.1 Parameter guarantee — 12.2 Preconditions

There is a systematic way to know if a given system operation must have a parameter guarantee precondition (or exception). This feature is also related to the operation’s functional test, as seen later in this book. The team must look at each parameter of the operation and ask if there are any valid and/or invalid values considering the type of the parameter.

As an example, let us consider the third operation in our example sequence diagram: set_assessment(selected_sending, user_id, updated_assessment). The types are absent from the expression, but they are easy to infer: • selected_sending: SendingId. The class Sending does not have a «unique» attribute, and although identifying its instances by looking at the reviewer and proposal is possible, it demands a lot of work. Thus the solution of creating an id:SendingId unique attribute for this class may solve the problem in an easier way. In fact, every class could have its unique attribute, but they are not always necessary. That is why they are created as the demand arises. In case of need, they can be used by the interface to uniquely identify an instance. However, the user must never have access to this value.

- user_id: PersonID. Remember that this is a unique code for identifying users and that it is not recommended to use codes that are known in the real world, such as social security number. This is so because the government may change the format of this number or even extinguish it without notice and also because people outside the United States usually do not have this identification number. Thus it does not serve for identification purpose in our system.

- updated_assessment: String. This is simple, except if we are considering that the updated text must have a minimum size. However, as the assessment is not necessarily sent just after being updated, we can accept at this point any size of text and leave the verification of its size to the operation that concludes the assessment.

The first and second variables of this operation have a very similar case: both receive a value that must conform to validity rules and that must correspond to valid objects stored by the system. For both cases, there is one class of valid objects (id’s that correspond to a valid object of the respective kind in the system) and one class of invalid objects (id’s that do not correspond to any valid object of the respective kind in the system).

In the case of the third parameter, at this time, any string can be accepted. Thus there is one class of valid objects including every string and no invalid class. Now, there is a rule:

For each invalid class comprehended in the parameters, the contract of this operation MUST have one precondition or exception to deal with it.

We will explain the issue with exceptions later. They are interchangeable. But let us concentrate on the preconditions for now.

The first parameter has one invalid class; thus, the precondition must certificate that this is not the case. The same happens to the second parameter. The third parameter does not demand the creation of any precondition for now. Thus the declaration of this operation with its preconditions could be like:

```ocl
Context Controller::set_assessment(selected_sending, user_id,
                                    updated_assessment)
    pre:
        self.person.assessments.sending->exists(a_sending|
            a_sending.id = selected_sending
        ) AND
        self.person->exists(a_person|
            a_person.id = user_id
        )
```

Abbreviated form:

```ocl
Context Controller::set_assessment(selected_sending, user_id,
                                    updated_assessment)
    pre:
        person.assessments.sending->exists(
            id = selected_sending
        ) AND
        person->exists(
            id = user_id
        )
```

### 12.2.2 Semantic and syntactic preconditions — 12.2 Preconditions

Regarding parameter guarantee preconditions, special care must be taken not to confuse semantic preconditions with simple syntactic verifications. Semantic preconditions require that the database is consulted: for example, verifying if there is a person with a given id. However, syntactic verification may be done preferably by mechanisms other than preconditions.

If a parameter has a type Natural, it is not necessary to query a database to verify if a given argument belongs to the type or not, because it is sufficient to ask if it is an integer greater than zero to reach that conclusion. Then, when a parameter is declared as x:Natural, it is not necessary to write any preconditions to assure that x is a positive number: the type already states that.

Another example is the ISBN, which has a formation rule, and can be checked syntactically. Instead of writing preconditions to verify if a parameter is a well-formed ISBN, the team should simply create a primitive type ISBN with a verification method and use it forever.

What about PrimeNumber? Could it be a type? The answer is yes, because to know if a given number is a prime number, a syntactic verification is sufficient. Simply verify if any prime minor or equals to its half divided by it produces an integer number. If it has an integer divider, then it is not a prime number. No databases must be consulted.

Types must be defined in the system operation signature. If the desired type does not exist, a primitive type can be defined by the team. For example, Fig. 12–1 uses primitive types such as IdProposal, MotivationText, and DecisionType^2 that may incorporate not only identification and checksum mechanisms but also security mechanisms, because those identifiers could be encrypted to avoid unauthorized access. In both cases, primitive types could be defined to deal with the complexity of the verification mechanism.

### 12.2.3 Complementary constraints — 12.2 Preconditions

A complementary constraint consists of assuring that certain constraints stronger than those of the conceptual model are valid while a given command is performed. Thus if the

2 Their description, however, do not appear in the diagram.

conceptual model states that a given role has multiplicity 0.1, for example, a complementary constraint could just say that when performing a given command that role is filled (1) or not (0). For example, in general, a Sending may have zero or more ProposalAssessment associated with it. But the command that finalizes a Sending could have a precondition that states that at least a minimum number of ProposalAsssessment is linked to it. This number can be a constant (e.g., 4) or a system variable, such as Sismob.minimum_assessments.

A precondition can never contradict the conceptual model. If the conceptual model states 0.1, then no precondition could state a multiplicity of 2 or more for the same role. But if the conceptual model states 0.2, then the precondition can further restrict it, stating, for example, 0.1 or 1.2, or even, just 0, 1, or 2.

### 12.2.4 Precondition assurance — 12.2 Preconditions

As the preconditions are not tested by the command that declares them, an external mechanism should exist to assure that they will be guaranteed before the operation is called.

This guarantee can be made by explicitly calling a query that verifies if the condition is true before calling the operation or by interface mechanisms that prevent the operation from being called with invalid data.

For example, instead of allowing the user to type any string in an ISBN field, the user could be led to select from a list of valid ISBNs, also with other information about books, such as, title, author, and price. That way, the parameter ISBN would be validated before performing the command that places one copy of that book in the shopping cart.

Usually, the flow of messages expressed in the system sequence diagram is a way to verify if preconditions are valid. For example, in Fig. 12–2, observe that the user_id is valid because the use case has a precondition that states it. Unless one of the operations in the sequence diagram deletes that user, it may be assumed that it continues to be valid until the end of the sequence. In some cases, concurrent processes by other users may be considered. It should be the case that a concurrent process deletes the instance. In this case, protections such as atomic transactions can be used or simply the observation that a given instance can never be deleted because of structural constraints.

## 12.3 Exceptions

*Chapter 12 · p. 224*

Exceptions in contracts are fail conditions that the designer cannot or does not wish to avoid before starting performing the command itself.

Sometimes, conditions identified as exceptions may be converted into preconditions. If it is possible to transform an exception into a precondition, it is generally advisable to do so, because it is preferable to avoid problems as soon as possible. It is preferable to keep the user from performing a mistaken action rather than allowing her to do it and then reporting the error later.

OCL does not present a specific expression to manage exceptions, but they can be simulated in contracts by conditional postconditions (Section 12.6) such as:

```text
post:
    if <condition> then
        <raise exception>
    else
        <all other post conditions, including other exceptions>
    endIf
```

As it would not be easy to represent many exceptions using this nested approach, we propose a new stereotyped expression, exception:, which is a shorter version of the expression above:

```text
exception
  <condition> IMPLIES <raise exception>
```

Now, for a contract to indicate an exception, it is sufficient to identify the condition that produces the exception and name the exception. Those names are usually represented by a code in a dictionary, and this code appears in the contract instead of the description.

A contract just indicates that exceptions may occur, but their handling must be defined only during the design of the interface or application tier, because if an exception is raised by the façade controller, it should be handled by the tier immediately above: the application or interface tier.

Imagine then in the contract for set_assessment it was not possible to guarantee that the Sending being passed as argument was not deleted by any other thread. In this case, instead of considering its existence as a precondition, the contract should indicate that it will try to use it, and if it by any chance does not exist, an exception will be raised. The partly defined contract with this exception would be something like:

```ocl
Context Controller::set_assessment(a_sending, a_user, updated_assessment)
    pre:
        self.person->exists(a_person|
            a_person.id = a_user
        )
        …
        NOT self.person.assessments.sending->exists()
        IMPLIES Exception.throw(E235)
        )
```

 )

Here, a basic throw message is used to signal the exception to a class named Exception, which is not a basic OCL class, but that can be created to manage exceptions. Notice that when a precondition is transformed into an exception, the condition itself is always negated.

It is assumed that when an exception is raised, the system operation cannot be executed and none of its postconditions or results are obtained, because the data must be kept in a consistent state even when an exception occurs.

Some exceptions may be converted into preconditions if the designer devises a way to assure the condition before calling the command. In this case, the condition is negated again. But remember that NOT NOT condition is the same as condition.

Only conceptual elements (concepts, attributes, and associations) may appear in the OCL expressions of the contracts. These elements are necessarily related to the business rules of the system being analyzed. The exceptions mentioned here must be exceptions related to the business rules and not exceptions related to hardware or communication problems. Exceptions that may occur in physical storage, communication, or external devices must be addressed by specific mechanisms in the tiers where those elements belong. Usually, users are not even aware of them.

## 12.4 Preconditions and exceptions versus invariants

*Chapter 12 · p. 226*

Invariants are used in the conceptual model to represent rules that should be always valid, independently on any system operation. Preconditions and exceptions are used for rules that are valid only during the execution of a given system operation.

When an invariant already exists in a given class, it is equivalent to the existence of an exception rule for each of its methods. For example, if there is an invariant that states that a student may enroll only in courses related to her career, then this invariant works as an exception in any method implemented in this class. Thus commands for enrolling a student may consider that the exception already exists in the form of the invariant, and if the student tries to enroll in a course that does not belong to her career, an exception would be raised.

Thus an invariant is equivalent to a set of exceptions, but not equivalent to preconditions. The existence of an invariant does not assure that the design or the user does not try to violate it. When an invariant violation happens, an exception is raised, just as in the case of exceptions. However, an operation may add a precondition that states that the invariant is assured before this operation is executed. This is a complementary mechanism that states that in the case of that specific operation, the invariant will not be violated because it has already being guaranteed by the design of the code.

Test mechanisms can be defined to verify if the invariants, preconditions, and postconditions are not being violated during the system execution. If those conditions are violated at any moment, they would raise exceptions. In those cases, the designer of the code must revise the structure of the program to correct the defect or handle the exception so that it will not happen again. When the system is delivered to the final user, it must be assured at the best of the team’s capacity, that no invariant, precondition, or postcondition is violated at any time.

Exceptions, however, may occur because of concurrency issues or as the result of failures, not bugs. For example, the code may be bug-free, but even so the network may be down. This is an exception that must be raised and treated, and it is not due to a failure in programming. This has to do with fault tolerance.

## 12.5 Query return

*Chapter 12 · p. 227*

As mentioned before, system commands change data while system queries just return data to the user. The contracts for system queries must define what is returned, and this can be done in OCL by using the body expression.

Expressions that represent preconditions are all Boolean, but expressions that represent the return of a query may have other types. They can return strings, numbers, lists, tuples, or even more complex structures. The following examples are based on the models of Figs. 12–1 and 12–2. Initially, we present the query that returns the list of sendings associated to a person as a reviewer.

```ocl
Context Controller::list_sendings(user_id:ID):OrderedSet<DTO_sending>
    pre:
        self.person->exists(a_person|
            a_person.id = user_id
        )
    body:
        self.person->select(:a_person|
            a_person.id = user_id
        ).assessments.sending.proposal->collect(:a_proposal|
            Tuple {
                name = a_proposal.name
                status = a_proposal.status
                priority = a_proposal.priority
                validity = a_proposal.validity
            }
        )->asOrderedSet
```

Abbreviated form:

```ocl
Context Controller::list_sendings(user_id:ID)
    pre:
        person->exists(
            id = user_id
        )
    body:
        person->select(
            id = user_id
        ).assessments.sending.proposal->collect(
            Tuple {
                name = name
                status = status
                priority = priority
                validity = validity
            }
        )->asOrderedSet
```

This query introduces two new functions of OCL, collect and Tuple. Collect is a function over collections that takes each element of the original collection and puts in the target collection the result of the expression evaluated inside parentheses. For example: {1, 2, 3, 4, 5}- . collect(x|2 3 x)

produces {2, 4, 6, 8, 10}. Applying it to collections of objects the idea is the same, an expression such as self.person- . collect(a_person|a_person.email) will return the set of emails of each person in the set self.person.

In fact, collect and the dot notation produce the same result. But the dot notation can be used only when the operation after the dot is postfixed (the operator goes after the expression.)

For example, we can write: self.person.email or self.person- . collect(a_person|a_person. email). Both expressions produce the same result.

However, an operation that is not postfixed, such as “ 3 ,” which is infixed (the operator goes between operands) cannot be written with the dot notation. For example, writing {1, 2, 3} 3 2 is not syntactically correct in OCL. It must be written as {1, 2, 3}- . collect(x|x 3 2).

The expression “Tuple” is not postfixed too; it is prefixed because the operator comes before the parameters. Tuple defines a kind of a key/value set, where the key is any identificatory chosen by the team, and the value must be a valid OCL expression that returns an object, data structure, or attribute value.

In the query before, a tuple is created with four keys: name, status, priority, and validity, and the respective values are all taken from the Person’s neighboring class Proposal.

It is recommended that system queries never return objects to the interface to keep both tiers logically separated. For example, instead of returning an instance of Person, the system query should return a simplified version of the information, such as a tuple with the values of the attributes of an instance of Person. There are some techniques that can be used to transform any OCL expression into simple data structures with alphanumeric values, such as JSON, XML, and proxies DTOs^3 .

## 12.6 Postconditions

*Chapter 12 · p. 228*

Postconditions establish what changes in the information managed by the system after some command is performed. Postconditions also must be carefully specified in terms that can be immediately recognized on the conceptual model structures. Thus although contracts can be written in natural language, they should be carefully written so they can be immediately translated into OCL expressions.

In order to classify the types of postconditions that can be used in a contract, we must take into account that the conceptual model has three basic elements, which are concepts, attributes, and associations. Thus considering that instances of classes can be created and destroyed, association links can be added, removed, and replaced, and attribute values can be changed, only six types of postconditions are necessary to express any change in data:

- Change an attribute value.

- Create a class instance.

> *Footnote 3:* Data Transfer Objects are a design pattern that indicates that objects passed by the façade controller to the interface and vice versa cannot be instances of conceptual classes (those in the conceptual model). They must be pure data, with no behavior attached. This may be implemented with objects that only have attributes and their respective getters and setters (if any), nothing else. The JSON structures and the OCL Tuple are examples of DTOs.

- Destroy a class instance.

- Add an association link.

- Remove an association link.

- Replace and association link.

These postconditions are the most fundamental or basic commands that may be defined for an object-oriented system. They may not be decomposed any further, and all other commands are defined as combinations of them.

Thus a basic command is a command that performs one of the six postconditions listed above. The meaning and behavior of a basic command are predefined.

The basic commands, as defined in the following subsections, are effectively basic in the sense that they do the task without performing certain consistency verifications. For example, a command that adds a link between two objects would not verify if the upper bounds for both roles of the association were surpassed. That kind of consistency verification is preferably made by preconditions or exceptions in the contract, and the design of the contract should not violate them.

### 12.6.1 Changing an attribute value — 12.6 Postconditions

One of the basic postcondition types consists of indicating that the value of an attribute was changed. That is usually written in OCL as 

```text
object.attribute = value
```

But, as OCL is a declarative language, this expression must not be understood as an assignment. It has, in fact, three possible ways to become true:

- object.attribute may be changed to become equal to value. This is usually the default interpretation.

- value may be changed to become equal to object.attribute.

- Both value and object.attribute may be changed to a third value and become equal.

Therefore in terms of code generation, this kind of expression may produce ambiguous interpretations. Cabot (2007) proposes a default semantic for interpreting such expressions so that ambiguity is reduced. However, another approach is possible, which does not require changing the original semantics of OCL. The idea is to use the “^” (caret) predicate instead of the “ 5 ” (equals sign) predicate, as explained below.

We can indicate without ambiguity that an attribute was changed just by declaring that a basic message concerning the change was sent to the object. The basic message is predefined, and its name should start with the prefix “set” followed by the name of the attribute. The new value is passed as an argument.

The message set_attribute may be sent to an instance of a class that contains the attribute. For example, if we are interested in changing the priority of a given Proposal, the following OCL expression could be used:

```ocl
Context Controller::change_priority(a_proposal_id:ProposalId,
                                    a_priority:Natural)
    post:
        self.person.proposals_sent->select(b_proposal|
            a_proposal_id = b_proposal.id
        ).priority = a_priority
```

But we have already seen that it can be interpreted in ambiguous ways. The expression below expresses the same intention but without any ambiguity:

```ocl
Context Controller::change_priority(a_proposal_id:ProposalId,
                                    a_priority:Natural)
    post:
        self.person.proposals_sent->select(b_proposal|
            a_proposal_id = b_proposal.id
        )^setPriority(a_priority)
```

Abbreviated form:

```ocl
Context Controller::change_priority(a_proposal_id, a_priority)
    post:
        person.proposals_sent->select(
            a_proposal_id = id
        )^setPriority(a_priority)
```

The caret notation means that the message at the right was sent to the object or collection of objects at the left. Thus it is a Boolean predicate, and the result of the expression above is Boolean.

All these postconditions could be simplified if there was a qualified association between the Controller and the class Proposal, as seen in Fig. 12–3.

In this case, the postcondition could be written as:

```ocl
Context Controller::changePriority(a_proposal, a_priority)
    post:
        all_proposals[id].priority = a_priority
```

**Figure 12–3: A qualified association between the controller and the Proposal class.** *(p. 230)*

> **Diagram content (transcribed from the figure image):** Fragment: Controller with qualified association by id → 0..1 all_proposals Proposal, plus */{ordered} proposals_by_deadline; Proposal * proposals_sent — 1 municipal_manager Person {+id: PersonId; +name; +email}; federal_manager, sendings_received and reviewer roles continue below.

Or:

- 

```ocl
Context Controller::changePriority(a_proposal, a_priority)
    post:
        all_proposals[id]^setPriority(a_priority)
```

The expression all_proposals[id].priority 5 a_priority means that two values are equal no matter how that result was accomplished. But all_proposals[id]^setPriority(a_priority) states unambiguously that the attribute priority of object all_proposals[id] was changed to a_priority.

This form of writing is still considered a declarative specification, not imperative. The expression with “^” just states that an object has received a message; it does not say who sent that message. The decision about which object is going to send that message is left for dynamic modeling (Chapter 13).

### 12.6.2 Creating an instance — 12.6 Postconditions

The command that creates an instance must just do that: create a class instance. Although OCL is not an imperative language, it has a constructor to indicate that a new instance of a class was created. This is expressed as a property of an object and is referenced as follows:

```text
object.oclIsNew()
```

Its meaning, when used in a postcondition, is that the object was created during the command being specified by the postcondition. This property may be used in conjunction with another that declares the class of the object:

```text
object.isTypeOf(Class)
```

However, as it would be a bit tedious to keep declaring the creation of an instance using two expressions, the definition of a single predicate that states that an object was created as an instance of a given class is suggested. The expression object.new_instance_of(class) is therefore defined as being equivalent to:

```text
object.oclIsNew() AND object.oclIsTypeOf(class)
```

Thus a postcondition that declares that a new instance of Person, referred to as new_person, was created can be defined as new_person.new_instance_of(Person).

In this case, the caret notation is not used because it is not a message sent to an instance of Person. It is a declaration that an instance new_person of class Person was created.

The message new_instance_of does not say anything about the instance’s attributes and links, even the mandatory ones. As before, it can be assumed that other expressions will initialize mandatory attributes and links, and that the new instance’s consistency will be checked for the contract as a whole and not for each individual basic command.

Attributes with initial values are considered automatically initialized when the instance is created. Thus it would be redundant to specify postconditions to update the attributes with initial values, unless values different from the default are desired.

Derived attributes, on the other hand, are calculated and cannot be directly modified. Thus they are not initialized too.

Attributes stereotyped with «optional» may be kept undefined at creation time; defining a value for them is not mandatory and usually is avoided.

But what happens with other (normal and mandatory) attributes when an instance is created? The basic command represented by the predicate new_instance_of simply produces the instance. It does not initialize attributes and links except for those that are defined with default initial values. If mandatory attributes and links are not initialized, the instance may be inconsistent; thus the contract should specify further postconditions that assure that all mandatory attributes and links are initialized when an object is created.

We have seen so far postconditions to create instances and change attributes. This allows us to combine them to create a contract for a CRUDL command that creates a new instance of Person. The system command create_person may have the following as a contract:

```ocl
Context Controller::create_person(person_id:PersonID, a_name:String,
                                  an_email:Email)
    post:
        new_person.new_instance_of(Person) AND
        new_person^set_id(person_id) AND
        new_person^set_name(a_name) AND
        new_person^set_email(an_email) AND
        self^add_person(new_person)
```

Thus this contract establishes that when the message create_person is sent to the controller, some modifications happen in the information structure. A new instance of Person was created, and its mandatory three attributes are initialized. An association from the controller for this class is mandatory from the site of the controller, and despite it being not able to navigate in that direction, it must be created anyway. Thus the message add_person sent to the controller establishes a link between it and the new person.

This class has other associations besides that with the controller, but they are all optional from the side of Person and do not need to be added at creation time.

### 12.6.3 Destroying an instance — 12.6 Postconditions

Although destroying objects is rare in object-oriented systems, it may sometimes occur. Usually, past deadline proposals and rejected proposals are not deleted physically: they are simply marked as inactive. In the Sismob project, this is even a supplementary requirement: no object is destroyed. Only data protection laws recently have introduced with more emphasis the need to really destroy information in a system.

Considering that an instance of an object is to be destroyed physically, there are two approaches to do it:

- Explicit: It is declared that the object was destroyed by sending an explicit destruction message to it.

- Implicit: All associations to the object are removed so that it becomes inaccessible. In programming languages, it is possible to implement garbage collection to remove from memory objects that are not accessible anymore.

In this book, the explicit approach is chosen because it makes the modeler’s actual intention clearer. An object that has to be destroyed, then, must receive a basic message such as the following:

```text
object^destroy()
```

The meaning of this expression is that the referred object was destroyed during the execution of the command.

It is assumed that all links to the destroyed object are removed as well. If any object formerly linked to it becomes inconsistent, then the contract must specify what happens to that object (if it is removed as well, or if the role is replaced by a link to another object). If there are objects that depend on the destroyed object, there are three options, which will be detailed later in this chapter:

- Precondition: the destruction of the object is prevented if it has dependent objects.

- Exception: the operation may try to destruct the object, but if it detects dependent objects, it fails.

- Postcondition: the operation removes the object and any other object that depends directly or indirectly of it. This option is not applicable in all circumstances, though.

### 12.6.4 Adding a link — 12.6 Postconditions

As mentioned earlier in the chapter, another kind of basic command is one that states that a link was added between two objects. Although link additions are bounded by the multiplicity of the roles, this is only checked for the contract as a whole and not for each individual basic command. Thus a basic command can surpass the upper limit of a role only if another command in the same contract removes one element from that role, maintaining the number of objects in the role within the limit.

Usually, an OCL postcondition to indicate that a link was created would look like the following:

```text
object.role->includes(another_object)
```

But, again, this expression may be ambiguously interpreted at the code generation stage, because there are at least four ways for it to become true:

- Include another_object in object.role.

- Assign to another_object an object that is already in object.role.

- Assign a third object to another_object and include it in object.role.

- Assign the empty set to another_object, because independently of the contents of object.role, it includes the empty set.

Usually, the first option is the intended meaning. But again, we suggest a notation that does not cause ambiguous interpretations and at the same time is more familiar to software developers. Once again, the “^” notation and a basic command are used to indicate that a link was created.

There are many dialects for naming commands that modify association roles. Here, we use the prefix add followed by the name of the role. Another common option would be to use the set prefix, as in the case of attributes. However, attributes have their values changed, while links are added; thus, perhaps, different goals should have different names.

Considering the association between classes Person and Proposal, and considering two instances, a_person and a_proposal, respectively, a link between the instances may be created in two different ways. First, from the point of view of a Person:

```text
a_person^add_proposals_sent(a_proposal)
```

The use of the role “proposals_sent” assures that the person is a municipal manager. Second, from the point of view of a Proposal:

```text
a_proposal^add_municipal_manager(a_person)
```

Both expressions are symmetric and produce exactly the same result: a link based on the association is created between the instances, and it is not directional.

Associations with mandatory roles, such as the one from ProposalAssessment to Person, usually require that their links are created in the same contract that creates the object that must have the role filled. Thus a link from ProposalAssessment to Person will be added always when an instance of ProposalAssessment is created, as shown below:

```ocl
Context Controller::create_assessment(a_person_id:PersonID,
                                      a_sending_id:SendingID,
                                      a_text:String, an_opinion:String)
    post:
        new_proposal_assessment.is_instance_of(ProposalAssessment) AND
        new_proposal^set_text(a_text) AND
        new_proposal^set_opinion(an_opinion) AND
        self.person->select(a_person|a_person.id = a_person_id)
            ^add_assessments(new_proposal_assessment) AND
        self.all_proposals.sending->select(a_sending|
            a_sending.id = a_sending_id
        )^add_assessments(new_proposal_assessment)
```

#### Abbreviated form:

```ocl
Context Controller::create_assessment(a_person_id, a_sending_id,
                                      a_text, an_opinion)
    post:
        new_proposal_assessment.is_instance_of(ProposalAssessment) AND
        new_proposal^set_text(a_text) AND
        new_proposal^set_opinion(an_opinion) AND
        person->select(id = a_person_id)
            ^add_assessments(new_proposal_assessment) AND
            all_proposals.sending->select(
                id = a_sending_id
            )^add_assessments(new_proposal_assessment)
```

**Figure 12–4: A simple model with mandatory and optional associations.** *(p. 235)*

> **Diagram content (transcribed from the figure image):** Controller —(one-way) 1 — * Car {+id: CarId} and 1 — * Person {+id: PersonId}; Car * fleet — 1 owner Person; Car 0..1 way_of_transport — * passenger Person.

As can be seen, the postcondition states that a new instance of ProposalAssessment is created. There are two mandatory attributes (text and opinion) that are initialized with the values received as arguments. There are also two mandatory associations to Sending and Person that must be filled with a link. The link between the Person and ProposalAssessment is easier to create because a Person can be directly identified by its id, and the link between ProposalAssessment and Sending is a bit more indirect, because, first, the controller should access all proposals and then localize a specific assessment attached to one of them.

### 12.6.5 Removing a link — 12.6 Postconditions

A single operation of removing a link can only be executed when an optional association exists between two objects. If the association is mandatory in one side at least, the link cannot be removed, but replaced to keep the consistency of the conceptual model.

All associations in the current example of Sismob have at least one mandatory role. Thus they do not serve as example to this basic operation. Let us then consider a situation where a Car has an owner (mandatory) and a number of passengers (optional). Se Fig. 12–4 for it.

As the figure shows, the association fleet/owner is mandatory, and it cannot be removed by a contract or an instance of Car would be inconsistent without an owner. This association can only be replaced, that is, we can substitute an owner by another. However, the association way_of_transport/passenger can be removed (if any exist) because it is not mandatory.

The removal of a link between two objects is made by a basic command prefixed by the word remove,^4 followed by the role name and receiving as a parameter the object member of the role that must be removed.

Then, a contract to remove a certain person from a certain car could be written like this:

> 

```ocl
Context Controller::remove_passenger(a_person_id:PersonId, a_car_id:CarId)
    def:
        a_car = self.car->select(:b_car|b_car.car_id = a_car_id)
        a_person = self.person->
            select(:b_person|b_person.person_id = a_person_id)
    post:
        a_car^remove_passenger(a_person)
```

> *Footnote 4:* Some dialects might use unset.

Abbreviated form:

```ocl
Context Controller::remove_passenger(a_person_id, a_car_id)
    def:
        a_car = car->select(id = a_car_id)
        a_person = person->select(id = a_person_id)
    post:
        a_car^remove_passenger(a_person)
```

In this case, if this person is not currently a passenger of that car, an exception would be raised. When the multiplicity of the destination role of the link to be removed is 1 or 0.1, it is optional to inform the parameter, because there is only one possible link to be removed. If instead of removing the link from the point of view of the Car, it was done from the point of view of the Person, the result would be the same, but the basic command would not need a parameter:

```ocl
Context Controller::remove_passenger(a_person_id:PersonId)
    def: a_person =
        self.person->select(b_person|b_person.person_id = a_person_id)
    post:
        a_person^remove_way_of_transport()
```

Abbreviated form:

```ocl
Context Controller::remove_passenger(a_person_id)
def: a_person = person->select(id = a_person_id)
post:
    a_person^remove_way_of_transport()
```

### 12.6.6 Replacing a link — 12.6 Postconditions

It is clear that replacing a link can be obtained by removing and adding a link, but this is an operation so important that it deservers to be included in the group of the basic commands.

Replacing a link can be used even when one of the roles is mandatory. It is considered an atomic operation, and thus, the mandatory role does not become inconsistent. One thing, however, that must be observed is if the role is immutable or not. It depends on the semantics of the model. Fig. 12–5 shows two situations, one where replacing a role is possible and other where it is not.

**Figure 12–5: A mutable and immutable role.** *(p. 236)*

> **Diagram content (transcribed from the figure image):** Car * — 1 Person (mutable link) vs Payment * —«imm»— 1 Sale (immutable link: a payment's sale cannot be changed).

This decision is totally dependent on the interpretation of the association. In the left side we have a car that must have an owner. We cannot add a second owner and neither remove the only owner for a period of time because during that period, the objects would be inconsistent. This is the case where the replace basic command can be used. Suppose that a_car is an instance of Car and a_person is an instance of Person. We could write an OCL expression such as a_car^replace_owner(a_person), which would change the former owner of this car by another one. This can be made because cars can change owners.

However, in the case on the right of the figure, an installment necessarily belongs to a sale, but contrary to the situation with cars and persons, an installment once attached to a sale cannot have its sale replaced by another one. Once an installment is added to a sale, there it remains.

### 12.6.7 Well-formed postconditions — 12.6 Postconditions

If we assume that the basic commands do not check if the objects and links are left in a consistent state, then the team must assure this verification when they are specifying the system command contracts.

The verifications that must be done are, at least, the following:

- A command that creates an instance must also have postconditions stating that all the instance attributes were initialized, except for (1) derived attributes (which are calculated), (2) attributes with an initial value (which are predefined by an init expression, unless a different value is desired), and (3) optional attributes, which can be null (in that case, initialization is optional too).

- All mandatory links for a newly created instance must be added.

- If after that the newly created object does not have a direct or indirect path to the controller, one must be created by one or more links.

- All created links must stay within the lower and upper bounds defined by their association roles multiplicity.

- All invariants affected by changes in attributes, links, or instances must not be violated, if possible.

The invariant-checking mechanism does not assure that the designer is writing a contract that keeps all invariants true. It is the responsibility of the designer to be aware of the invariants and avoid raising unnecessary exceptions. If an invariant happens to raise an exception that is not handled by the system, then there is certainly a design problem. Thus when it is impossible to prevent an exception, at least it must be handled by the upper tier (the interface).

Another issue involves attributes declared with initial values. If the definition of the initial value of an attribute uses information that may be obtained only by navigating its links, how can it be calculated before the links are created? The team must consider that the initialization of attributes with initial values will be one of the last tasks in the programming code that implements a contract, that is, attributes with initial values may be defined only after all links are added and the instance is (almost) consistent. In Fig. 12–6, it can be seen that the Item.value attribute may only have its initial value assigned after a link between the instance of Item and Product is added. Otherwise, the value of the attribute would be undefined.

**Figure 12–6: An example of an initial value that depends on another object.** *(p. 238)*

> **Diagram content (transcribed from the figure image):** Product {«imm» «unique» +id: ProductId; +catalog_value: Money} 1 — * Item {+quantity: Natural; +value: Quantity = self.quantity*self.product.catalog_value} * — 1 Order {«imm» «unique» +nr: OrderNr; «imm» +date: Date}.

### 12.6.8 Combination of expressions — 12.6 Postconditions

Usually, OCL expressions used in preconditions, postconditions, exceptions, and body may be joined by the AND operator. This means that all expressions in the chain of ANDs must be true.

But it is also possible to use the OR operator, which establishes that just one of the expressions must be true in order to the combined expression to be true. For example:

```ocl
Context Person::chose_wardrobe():String
    body:
        if System.rains() then
            “umbrella” OR “raincloath”
        else
            “normal clothes”
```

The problem with using this kind of expression is that it is inherently ambiguous. If it is raining, we cannot know for sure if the person is using an umbrella, a raincoat, or both. This kind of ambiguity is often avoided in usual information systems.

Another operator that can be used to connect OCL expressions is the IMPLIES operator, which has the same meaning of the implication operator of Boolean logic. IMPLIES is used when a postcondition is to be obtained only if a certain condition is true. For example, the following contract allows a user to change the text of a ProposalAssessment only if it is not concluded:

```ocl
Context Controller::change_assessment(a_person_id:Person_Id,
                    a_proposal_Assessment_Id:Proposal_assessment_Id,
                    a_text:String)
    def:
        person = self.person->select(a_person|a_person.id = a_person_id)
        assessment = person.assessments->select(an_assessment|
            an_assessment.id = a_proposal_assessment_id)
    post:
        NOT assessment.concluded IMPLIES
            assessment^setText(a_text)
```

Abbreviated form:

```ocl
Context Controller::change_assessment(a_person_id, a_proposal_Assessment_Id,
                                      a_text)
    def:
        person = person->select(id = a_person_id)
        assessment = person.assessments->select(
            id = a_proposal_assessment_id
        )
    post:
        NOT assessment.concluded IMPLIES
            assessment^setText(a_text)
```

Remember that the NOT operator has precedence over implication. Then, the postcondition may be read as “if the assessment is not concluded, then its text is changed.”

The advantage of implies is that it is shorter than if-then-endif, but they have the same meaning. The advantage of if-then-endif or if-then-else-endif is that it is more familiar to programmers and includes a way to specify what must be obtained for both cases of a Boolean expression that is shorter than using two implies structures.

### 12.6.9 Former values — 12.6 Postconditions

Sometimes a postcondition is built upon values that attributes and roles had before the command is performed. Those former values are referred to by the function @pre to indicate that they do not correspond to the value of the attribute after the command is performed (which could be different). For example, a postcondition that establishes that a quantity in stock for a given product has increased may be expressed as:

```ocl
Context Controller::add_to_stock(product_id:ProductId, a_stock:Natural)
    def:
        product = self.products->select(a_product|a_product.id = product_id)
    post:
        product^set_quantity(product.stock@pre + a_stock)
```

Abbreviated form:

```ocl
Context Controller::add_to_stock(product_id, a_stock)
    def:
        product = products->select(id = product_id)
    post:
        product^set_quantity(product.stock@pre + a_stock)
```

Thus why was @pre used above? Because after the command is performed, the quantity in stock would already be incremented, and the argument for the basic command must be defined as the previous quantity plus the new quantity. That is why we have to write product. stock@pre (the former value) instead of product.stock (the newer value).

Remember that OCL is declarative, just as arithmetic is. Ada Lovelace already noticed in the 1830s that x 5 x 1 1 is not a true statement in mathematical notation, because it cannot be true for any value of x. But when you write x 5 x 1 1 in a programming language, it means the same as x 5 x@pre 1 1.

### 12.6.10 Postconditions covering collections of objects — 12.6 Postconditions

It is possible with a single OCL expression to state that a whole set of objects was changed. For example, an expression that states that the price of every product was raised by x% may be written using the forAll expression:

```ocl
Context Controller::raise_product_price(x:Percent)
    post:
        self.product->forAll(:a_product|
            a_product^set_price(a_product.price@pre*(1+x))
  )
```

) )

If the price is going to be raised by a value that does not depend on its former values, such as M$0,50 for each product, then there is no need to use the @pre notation. For example, if the price of all products has to be raised by x mira, then the following expression could be used:

```ocl
Context Controll::add_to_product_price(x:Money)
    post:
        self.product->forAll(:a_product|
            a_product^setPrice(a_product.price + x)
```

 )

Remember that in our examples, product is a role of an association from the controller to the class Product.

### 12.6.11 Postconditions and real-world events — 12.6 Postconditions

The process of creating contracts is intimately related to the expansion of the use case and the conceptual model. The conceptual model should be used as a reference at every moment because it is the source of information with which assertions can be made about the information.

Contracts should be always written with expressions that can be interpreted in terms of elements of the conceptual model. Thus assertions like “the products were shipped” or “the product was lost” would hardly be postconditions because they do not represent information contained in the conceptual model; they describe real-world events. If the team wishes to express this in a contract, they should create a conceptual structure (attribute, role, or concept) to represent it. For example, the fact that the products were shipped could be represented by creating an instance of the Delivery class and linking it to the current instance of Order.

## 12.7 Pattern contracts for CRUDL

*Chapter 12 · p. 241*

The following subsections present models for contracts for typical CRUDL commands. There are three system command contracts and two system query contracts. The commands and queries examples are performed within the Person class, defined in accordance with the model of Fig. 12–7.

As in the case of CRUDL use cases, seen before, CRUDL system contracts can also be considered as patterns. It is our intention to show with this special model all contractual possibilities of these operations.

From now on, we abandoned the more verbose version of OCL to deal only with the most abbreviated version for each contract.

### 12.7.1 Contract for create — 12.7 Pattern contracts for CRUDL

The contract for a create command usually should include the instantiation of a new object, initialization of its mandatory attributes, and addition of its mandatory links. The list below summarizes what we have to do with each attribute and association in the example:

- Attribute id: must be filled with a parameter of the create function, or with a new number created by a system service class.

- Attribute name: must be filled with a parameter of the create function.

- Attribute date_of_birth: must be filled with a parameter of the create function.

- Attribute municipality_of_residence: nothing is done because it is a derived attribute.

- Attribute date_of_registry: it does not need to be filled now because it has an initial value that is calculated by the system. As it is also immutable, it would not be changed in the future.

**Figure 12–7: Basic conceptual model for examples in this section.** *(p. 241)*

> **Diagram content (transcribed from the figure image):** Controller with qualifier id 1 —(one-way)→ 0..1 Person {«imm» «unique» +id: PersonID; +name: String; «imm» +date_of_birth: Date; +/municipality_of_residence: municipality:MunicipalityName; «imm» +date_of_registry: Date = System.today(); «opt» +gender: Gender}; Person * —«temporal»— 1 Address {«imm» +street: String; «imm» +number: Natural; «imm» +municipality: MunicipalityName; «imm» +state: StateName; «imm» +country: CountryName}; Person 1 —«temporal»— 0..1 Passport {«imm» +number: PassportID; «imm» +name: String = person.name; «imm» +validity: Interval<Date>}.

- Attribute gender: as it is an optional attribute and not immutable, it does not need to be created now. It can be filled latter.

- Role address: as it is a mandatory role, when a Person is created, her Address must be defined at the same time. In some cases, especially when the association is mandatory in both ends, the attributes of the address should be passed together with the attributes of the person in a single operation that creates both objects simultaneously. But as the role to the side of Person is optional, we can create an Address independently, and then pass it as argument to the operation that creates a Person. Notice also that the same address may belong to more than one person.

- Role passport: as it is an optional role, it does not need to be filled now. It can be added later or never.

Now, let us see the contract for create an instance of Person accordingly to this model:

```ocl
Context Controller::create_person(an_id, a_name, a_date_of_birth, an_address)
1    pre:
2        person[an_id]->isEmpty()
3    post:
4        new_person.new_instance_of(Person) AND
5        new_person^set_id(an_id) AND
6        new_person^set_name(a_name) AND
7        new_person^set_date_of_birth(a_date_of_birth) AND
8        new_person^add_address(an_address) AND
9        new_person^set_date_of_registry(System.today) AND
10       self^add_person(new_person)
```

Lines were numbered to easy explanation. The precondition in line 3 establishes that there is no Person in this system with the same id as the one received as parameter. This is for avoiding violating the unique constraint in this attribute.

Line 4 established that an instance of Person was created. Lines 5, 6, 7, and 9 initialize the mandatory and nonderived attributes of this class. Finally, line 8 creates a link with the address passed as parameter, and line 10 creates a link with the controller. As this last one is unidirectional, it must be a message received only by the controller and not vice versa.

### 12.7.2 Contract for update — 12.7 Pattern contracts for CRUDL

The CRUDL update command usually involves changing the value of some attributes. Before defining a contract for updating an object, however, the team must check which attributes are immutable. Attributes and association roles with the «imm» stereotype cannot be changed by any command after the object is created. Those properties are read-only.

The update command then will change normal attributes that are not immutable, neither derived. In the case of a Person in Fig. 12–7, only the following attributes may be updated: name and gender. Regarding roles, they usually are changed by specific operations. For example, one operation could replace the address of the Person and another could add a new Passport. Usually this is not done by the CRUDL update. The update contract in this case might look like the following:

```ocl
Context Controller::update_person(an_id, a_name, a_gender,
                                  an_address, a_passport)
1    def:
2        a_person = person[an_id]
3    pre:
4        a_person->notEmpty()
5    post:
6        a_person^set_name(a_name) AND
7        a_person^set_gender(a_gender)
```

In this case, we defined a precondition in line 4 to establish that there is a person in the system with the id provided. Notice that this is the opposite of the precondition for the creation operation.

In lines 6 and 7, we update the value of the only two attributes that can be updated. Notice that in this case, it is not necessary to create a link between the controller and the instance of person, because it already exists.

The class Controller would have also operations to replace the Address and add a Passport to an instance of Person (passports usually cannot be replaced neither removed).

### 12.7.3 Contract for delete — 12.7 Pattern contracts for CRUDL

The command that deletes an object must consider structural rules of the conceptual model before deciding if an object can or cannot be destroyed.

In the case of Fig. 12–7, for example, an instance of Person cannot be deleted if one or more passports are linked to it, because, from the point of view of the passport, the link is mandatory. This does not happen to addresses, because an Address can exist without being linked to a Person. In this case, it is the Person that cannot exist without an Address.

Thus before planning to delete an object from the system, it is convenient to verify if there are associations that prevent this operation to be performed.

In order to perform deletion without violating any structural rules, one must choose one of these three approaches below:

- Assure by precondition that the object being deleted would not leave other objects inconsistent regarding the lower bound of their associations. With this approach, only persons with no mandatory associations to them may be deleted. In the example, a Person with no Passport may be deleted but a Person with a Passport should not be deleted so easily. It can be highlighted in the system interface: the objects that cannot be deleted may be gray or without the delete icon, while others have normal color and/or the presence of the icon.

- Use an exception to abort the delete command if it is attempted for an object that will leave other objects inconsistent. If a user tries to delete Person that has passports linked

to it, an exception would be raised. In this case, the interface shows every person and provides the delete option for anyone. But if the operation is tried on an object that cannot be deleted, an error message produced by an exception will appear and avoid the operation to be concluded.

- Assure by postcondition that all objects that would be left inconsistent after deletion are deleted as well in cascade. In this case, all passports linked to a Person to be deleted would be deleted as well.

The third approach is used when we want to propagate the delete command to every object that has mandatory associations to the object being deleted. This propagation is recursive: deletion will continue until no more objects with mandatory links to objects that were deleted are found.^5 This approach may not always be used; there are situations in which propagating deletion is against business rules. In the case of Persons, for example, deleting an Address linked to a person will leave that person inconsistent. However, it probably is not the case to propagate the deletion to the Person as well. In this case, what happens is that deleting an Address linked to a Person is prohibited. However, deleting a Person with all her Passports is acceptable, because if a Person is deleted, those Passports have no reason to continue to exist.

Let us see the three possible contracts to delete a Person. First one, prevented by precondition:

```ocl
Context Controller::delete_person(an_id)
1    def:
2        a_person = person[an_id]
3    pre:
4        a_person->notEmpty() AND
5        a_person.passport->isEmpty()
6    post:
7        a_person^destroy()
```

In line 4, the precondition states that the person exists, and line 5 states that it is not linked to any passport. Thus it can be deleted, as done in line 7.

Now let us see the contract where exception is used to prevent an invalid deletion to happen:

```ocl
Context Controller::delete_person(an_id)
1    def:
2        a_person = person[an_id]
3    pre:
4        a_person->notEmpty()
5    post:
6        a_person^destroy()
7    exception:
8        a_person.passport->notEmpty() IMPLIES Exception.throw(278)
```

5 In fact, in the general case, the lower bound of the role is the information that must be considered. For example, if a role has multiplicity 3.– , than removing a link when only 3 are left already makes the object inconsistent.

In this case, the precondition only checks if the person exists. Postconditions are tried to be achieved but cannot because an exception raises if a Passport is attached to the Person.

Finally, let us see how the deletion would happen if it were cascaded by preconditions. Remember that this option is not always valid, it depends on the semantics of the objects and their links. The contract is this:

```ocl
Context Controller::delete_person(an_id)
1    def:
2        a_person = person[an_id]
3    pre:
4        a_person->notEmpty()
5    post:
6        a_person^destroy() AND
7        a_person.passport^destroy()
```

As there are no other classes dependent to Person or Passport, so this is sufficient. Otherwise, a list of other objects to be deleted would be added to the post section of the contract.

A programmer used to imperative languages could find strange to destroy an object and then destroy the objects linked to the original one. In most imperative languages, it would be an error and the order of those expressions should be inverted. However, OCL is declarative, and the “AND” expression means really “and” and not “then” as in imperative languages. Thus the idea is not a sequential flow of commands, but a single logic expression glued by some “ANDs” that must be true after the operation is executed.

Observe also that the caret notation can be used with collections of objects, as in a_person.passport^destroy(). In this case, it is a set of objects (passports) that are declared as destroyed.

However, usually, information systems do not allow information to be deleted. A person that is removed from the system, for example, is not really deleted, but marked as inactive. For implementing this approach, one simple solution is to define a new Boolean active attribute for the class whose members may be inactivated instead of deleted. The default value for this attribute is true because the object usually is active when it is created.

### 12.7.4 Contract for retrieve — 12.7 Pattern contracts for CRUDL

The simple CRUD retrieve query returns information about the attributes of a class as they are; that is, without doing any calculation, filtering, etc. In this case, normal attributes, immutable, derived, and attributes with initial value, all of them can be returned. The exception would be private attributes, but they are not used yet in conceptual model.

These queries do not return data that are not explicitly in the class definition. Queries that return data calculated from one or more objects are reports, not retrieve queries.

A simple retrieve query for the class Person of Fig. 12–7 could be defined as follows:

```ocl
Context Controller::retrieve_person(an_id:):Tuple
    def:
        person = person[an_id]
    body:
        Tuple {
            id=person.id,
            name=person.name,
            date_of_birth=person.date_of_birth,
            municipality_of_residence=person.municipality_of.residence
            date_of_registry=person.date_of_registry
            gender=person.gender
        }
```

As discussed before, the retrieve query returns a tuple or record with the data from the attributes of the object selected by the query parameter.

### 12.7.5 Contract for listing — 12.7 Pattern contracts for CRUDL

Finally, the second query of CRUDL is a query that lists all objects belonging to a class or those that correspond to a Boolean filter. Usually, not every attribute will be shown in a listing. Thus the team may consult to user/client (or use the CSD matrix) to decide which attributes are relevant for a listing. Usually, only attributes that help the user to recognize the record she is looking for are used. In this example, we chose as attributes to locate a Person, the following items: name, date_of_birth, municipality_of_residence, and gender.

If no filter is applied, then every object will be listed. The contract in this case could be:

```ocl
Context Controller::list_person():Set<Tuple>
    body:
        person->collect (
            Tuple {
                name=person.name,
                date_of_birth=person.date_of_birth,
                municipality_of_residence=person.municipality_of.residence
                gender=person.gender
            }
        )
```

 } )

We discuss some patterns for the application of filters to listing later in the book.

## 12.8 Discussion

*Chapter 12 · p. 246*

An expanded use case is a chain of commands and queries that will be performed in a given sequence. Usually, each operation will supply information or assure preconditions for other operations. The best approach to write contracts for this sequence of operations is to follow the use case flow that is depicted in the system sequence diagram. In this sequence, the team must ask:

- What is the goal of each operation?

- What do they produce in terms of information?

- How do they change attributes and object links?

- Do they create or destroy or deactivate objects?

- What do they expect their predecessors have produced?

- Which exceptions could happen during execution?

- Can their exceptions be reconfigured as preconditions?

- Do their parameters include groups of values that are invalid? If positive, this demands preconditions or exceptions.

- Do the operations follow a known pattern?

When answering these questions, the designer will be building contracts that allow the commands and queries to be performed in a consistent way in the context of the use case transaction. If it is necessary to add new queries or commands to the sequence diagram to assure certain preconditions, then this is the right moment to do that.

## Questions (Chapter 12)

1. Explain and present an example on how an exception may be transformed into a precondition and vice versa.

2. What is the difference between exceptions in command contracts and in query contracts?

3. What are the six possible postconditions, and what basic commands define each of them?

4. In Fig. 12–2, although a Sending may have multiple assessments, they must all be from different reviewers. The current model does not guarantee it. Write an invariant that deals with this issue.

5. Give an example of a mandatory link that can be replaced and another that cannot be.

This page intentionally left blank

