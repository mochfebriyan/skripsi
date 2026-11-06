<!-- Knowledge file: Chapter 10 — From use cases to conceptual model -->
> **About this file.** Chapter 10 of a cleaned, AI-ready edition of Wazlawick, R. S. (2024). Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-443-13739-6.  
> **Covers:** Iterative construction of the conceptual model from expanded use cases: finding concepts, attributes and associations; dependent vs independent concepts; worked SISMOB example.  
> **Use this file when:** deriving a class diagram/ERD step by step from use cases or functional requirements.  
> **Sections:** 10.1 Iterative construction of the conceptual model (p. 165); 10.2 How to find concepts and attributes (p. 165); 10.3 Dependent and independent concepts (p. 168); 10.4 How to find associations (p. 169); 10.5 Example of iterative construction of the conceptual model (p. 169)  
> **Contains:** 4 figures transcribed as text, 3 code listings.

# Chapter 10: From use cases to conceptual model

*Source: Wazlawick, Object-Oriented Analysis and Design for Information Systems, 2nd ed. (Elsevier, 2024), starts p. 165*

## Key topics in this chapter (Chapter 10)

- Finding Classes and Attributes

- Discovering Associations

- Independent and Dependent Concepts

- Iterative Construction of the Conceptual Model

## 10.1 Iterative construction of the conceptual model

*Chapter 10 · p. 165*

This section shows how the conceptual model can be refined with information from the expanded use cases. Initially, we discuss how to find concepts and attributes from the use case texts. Next, we discuss how to identify new associations for the model. Finally, we present a complete example with some use cases from the first iterations of the SISMOB project and their contribution to the conceptual model.

## 10.2 How to find concepts and attributes

*Chapter 10 · p. 165*

The process of discovering the elements of the conceptual model may vary. However, one of the most useful techniques is to look at the text of the expanded use cases or system sequence diagrams. From those artifacts, one can discover all textual elements that eventually refer to information to be managed.

Usually, these textual elements are composed of nouns such as “person,” “order,” “payment” or by expressions that denote nouns (known in linguistics as noun phrases), such as “payment authorization.” Moreover, sometimes even verbs may represent concepts, when verbs express an act that corresponds to a noun, for example, the verb “to pay,” which corresponds to the noun “payment.”

The team should mind the project goals and scope when looking for the elements of the conceptual model. It is not advisable to represent information that is irrelevant to the system in the conceptual model. Thus not every noun, adjective, or verb should be considered as a model element. The team is responsible for understanding which expressions represent useful information for the system.

The process of identification of concepts and attributes consists of the following:

1. Identify in the expanded use case text or in the arguments of the operations in the system sequence diagram the words or phrases that correspond to concepts that are relevant to the system and therefore, must be maintained. 

167 

2. Group words or phrases that refer to the same entity, for example, “buy” and “acquisition,” “customer” and “client,” etc.

3. Decide which of the identified elements are complex concepts and which are mere attributes. Usually, attributes are the elements that may be considered alphanumeric (names, numbers, codes, monetary values, Boolean values, etc.), enumerations, or primitive (dates, ISBNs, etc.).

Even if there is no preliminary conceptual model, then, the first use case analyzed will be used to identify the first concepts. However, it is better if a structure like a preliminary conceptual model is available, because a better vision of the whole system is at hand in this case. If the preliminary conceptual model already exists, then the use cases will help to refine the model, indicating new concepts, new attributes, new associations, or structure changes.

If the team prioritizes the more complex use cases to be analyzed first, then significant new information may be added to the model quickly.

## 10.3 Dependent and independent concepts

*Chapter 10 · p. 168*

A concept is dependent from others if it needs to be associated to them to make sense, that is, to represent information that is minimally meaningful.^1 For example, an assessment, as a single instance of class Assessment, alone does not have a complete meaning; the author of the assessment could remain unknown, but the object assessed must be known so that the assessment is meaningful.

A concept is independent if it has a meaning even without being associated to others.^2 For example, the Person concept may be understood just from its attributes, without being associated to other concepts. The existing associations for a person are optional. Thus the Person concept, in that sense, is independent.

But what purpose does this distinction serve? It was discussed before that only the simplest concepts may be managed by CRUDL use cases. This definition in most cases will include independent concepts, that is, usually, independent concepts are manageable by CRUDL.

However, dependent concepts should not be considered so simple in principle, because they have to be associated to others from the beginning, and this introduces complexity.

Concepts that are managed by CRUDL use cases are usually those that can be accessed directly when information is being retrieved from a system. If the team uses the controllerfaçade class in the conceptual model, in principle, the independent concepts must have mandatory links to the controller class. Being linked to the controller class means that the instances of the class may be accessed directly by it. For example, an instance of Person may be accessed directly by the controller by using its id. However, an instance of Assessment is not necessarily accessible directly by the controller.

> *Footnote 1:* There is a parallel between dependent concepts and transitive verbs. The sentence “He opened” does not make sense, because the verb needs a complement, as for example, “He opened the can.”

> *Footnote 2:* A parallel exists between independent concepts and intransitive verbs. The sentence “He slept” makes sense because the verb does not require a complement. However, even intransitive verbs may have supplemental information (e.g., “He slept for 3 hours”), and independent concepts also may have such complements.

Therefore dependent classes in principle are not linked to the controller. But they may require a direct link in some cases. Although this is somewhat redundant, it may be the case. Fortunately, there are mechanisms to prevent this redundancy to become a problem.

## 10.4 How to find associations

*Chapter 10 · p. 169*

If the information related to concepts and attributes is easily found in the use case texts, this is not the case for associations. As mentioned before, use cases contain references to operations that transform information, but when it is the case for associations, they are not so easily found.

So, how do we find associations between complex concepts? There are at least two rules that can be used:

- Dependent concepts (such as Project, Assessment, and Cancellation) should be necessarily associated to the concepts that complement them (which may be dependent or independent). The role opposite to the dependent concept is usually mandatory in this case, meaning that dependent objects are created with that role already filled.

- Associative information, that is, associations that are not mandatory but that add new information to the model should be represented by associations. For example, Person and Car may be considered independent concepts; however, they can be associated by a variety of modes, such as “owner,” “driver,” and “passenger.”

Sometimes, associative information appears in the use case texts as concepts. For example, an order could be thought as an association between a customer and products, but it is sufficiently complex to be represented as a concept, because it has at least some attributes that must be owned by the association itself. In this case, an intermediary concept between Order and Product is necessary. If this intermediary concept is Item, then it should be associated to both Order and Product to make sense, because it is a dependent concept.

Let us talk a little about a mistake that sometimes happen. Complex concepts must be linked only by associations, meaning that one complex concept must not have an attribute typed with the name of another complex concept. If the team detects attributes with that characteristics, they should replace them by associations as soon as possible.

It is also not recommended to use alphanumeric attributes as foreign keys (Date, 1982). For example, if a Car has an attribute like owner_id:ID, we do not have the case of an attribute being typed by a complex concept name. However, the intention here is clear: the attribute owner_id is a reference to an instance of class Person. This must be avoided too, and this attribute is replaced by an association between the two concepts.

## 10.5 Example of iterative construction of the conceptual model

*Chapter 10 · p. 169*

Let us proceed with a demonstration on how to evolve and refine a conceptual model by using expanded use cases. First, let us recall the preliminary conceptual model for the SISMOB project shown in Figure 4–5 and now presented also in Fig. 10–1.

**Figure 10–1: Preliminary conceptual model serving as example.** *(p. 170)*

> **Diagram content (transcribed from the figure image):** Conceptual model after naming roles: Cancellation 0..1 — 1 Proposal; Proposal * — 1 sender MunicipalManager; Proposal 1 — * Sending; FederalManager 1 receiver — * Sending; Sending 1 — * ProposalAssessment; Sending 1 — 0..1 FundsAllocation; FundsAllocation 1 — 0..1 FundsDeallocation; FundsAllocation 1 — 0..1 Publication; FundsAllocation 1 — 0..1 PhaseCompletionRequisition 1 — 0..1 PhaseAssessment.

Notice that associations and their multiplicity are already present in the diagram as they were induced before by analyzing concepts and their dependencies. In this figure, we have already identified the roles of sender and receiver of a proposal, but they will be changed soon.

Initially, we should analyze the most complex use cases (save the CRUDL and reports for later). It is a temptation to start analyzing use cases by chronological order, starting, for example, with the use case that allows a municipal manager to introduce a proposal in the system. But we do not have to necessarily follow this order. Starting by the most complex use cases helps the team to cope with complexity in the beginning of the development process, and thus it may mitigate a lot of project risks as well as avoiding the need to refactor the model to accommodate complex use cases that were left to be analyzed later in the process.

So, we can begin by analyzing the use case already expanded in Chapter 6, “Produce proposal assessment.” First thing to do is to mark nouns, noun phrases, adjectives, and even verbs that are candidate concepts. This is done below by using underline or double brackets. Use Case: Produce proposal assessment (main flow)

1. «Reviewer» search for «process».

2. System presents list of «processes» allocated to reviewer, newest first.

3. Reviewer selects process.

4. System presents {process namec, «status», «priority», and «validity».

5. Reviewer registers assessment and «conclusion». [V1]

6. System confirms operation.

Variant V1: User decides to save for continuing latter.

V1.1 Reviewer registers assessment and saves it.

V1.2 System confirms that the assessment is saved. V1.3 Use case ends.

Exception E1: Deadline reached BR-FNS.01.

E1.1 System presents message MODAL.114. E1.2 User acknowledges. E1.3 Use case fails.

Exception E2: Proposal was not prioritized BR-FNS.06.

E2.1 System presents message MODAL.371. E2.2 User acknowledges. E2.3 Use case fails.

In this use case, specifically, only the main flow produced interesting candidates. We put brackets in “processes” in line 2 because there is a clue here that there are many assessments allocated to a reviewer (an association!) and that this queue is sorted or at least ordered.

Thinking about synonyms, maybe at this time the team would perceive that the term “project” is being used. Is this the same thing as “proposal”? The conceptual model uses that name to identify a concept that seems to coincide with the idea of project in the use case. As this is exactly the case, the team may rewrite the use case by replacing the term “project” by the more adequate term “proposal.” Who decides on the more appropriate name is the user/client.

In this example, one new concept is revealed: Reviewer (or may it be a role?). Proposal and Assessment already belong to the model. The terms “reviewer” and “project” are repeated in the text and do not need to be marked more than once. Moreover, new attributes of Proposal are discovered now: name, status, priority, and validity. They must be introduced in the conceptual model.

It was created also an enumeration, ProposalStatus, the values of which are not yet known. This lack of information could be written at this time at the CSD matrix as a doubt to be answered by users or client later if they are not available immediately.

Also, it is observed in line 5 that the assessment has a conclusion, and it is a strong candidate for an attribute: a flag that indicates the state of the assessment.

Notice also that the attributes concluded and text of class Assessment should be added.

Finally, and more subtle, as the user may search proposals directly and choosing one to work with it may indicate that proposals must have an unique identification, and therefore, a potentially hidden attribute, but let us leave it public for now.

A deeper exam of the use case may show that when information about a proposal is shown an incomplete assessment could also be shown so that the user may finish it. This demands a modification on the use case for better conformance.

Thus, before going to the conceptual model, let us see how the use case seems after those discoveries. Only the main flow was modified and is shown below.

Use Case: Produce proposal assessment (main flow)

1. «Reviewer» searches for «proposal».

2. System presents list of «proposals» allocated to reviewer, newest first.

3. Reviewer selects proposal.

4. System presents {proposal namec, «status», «priority», and «validity». It also shows the current saved version of the assessment if any, or empty string.

5. Reviewer updates assessment and «conclusion». [V1]

6. System confirms operation.

This revision of the requirements written in the use cases is normal and usually expected. And now, the refined conceptual mode can be seen in Fig. 10–2.

Now we are going to proceed with a change of perspective because as reviewers and federal and municipal managers are roles for people, it would be better to represent them as roles for the class Person. If those roles need any special attributes or associations later, they can be complemented by an association class each.

It can be seen in the model that Sending and ProposalAssessment should have a date each and that those dates must be not later than the date of the validity of the proposal. This can be represented by invariants in class Sending and ProposalAssessment. All those modifications are represented in Fig. 10–3.

Before analyzing another use case, let us observe that the role name “reviews” is applied to the class “ProposalAssessment.” Are “review” and “assessment” synonyms? If they are, we should choose just one term to continue. This issue should be discussed with the user or client. For now, let us consider that they are in fact synonyms and that we chose to use the term “assessments” but to keep the class name “Reviewer.” Thus the role name “reviews” must be changed to “assessments.”

Next, we are going to analyze another use case for the same system. As suggested before, we would leave CRUDL and reports for later and try to explore first use cases that can help discovering new concepts, attributes, and associations. The use case “Decide on proposal” is associated to the federal manager, and a business rule states that a decision can only be taken after at least three assessments are available and necessarily before the deadline of the proposal. Considering the decision, the happy path is to continue with the project, but variants such as cancellation or asking for modifications are also possible.

**Figure 10–2: First refinement.** *(p. 172)*

> **Diagram content (transcribed from the figure image):** Next iteration with attributes: Proposal {+name: String; +status: ProposalStatus; +priority: Natural; +validity: Date; «unique» «imm» +id: ProposalId}; «enumeration» ProposalStatus {? to be defined}; ProposalAssessment {+text: String = ""; +concluded: Boolean = False}; new class Reviewer with ProposalAssessment * — * Reviewer; other associations as Fig 10–1 (MunicipalManager sender, FederalManager receiver, Sending, FundsAllocation, FundsDeallocation, Publication, PhaseCompletionRequisition, PhaseAssessment).

**Figure 10–3: First refinement revised.** *(p. 173)*

> **Diagram content (transcribed from the figure image):** Iteration where actors become one class Person: Proposal {«imm» «unique» +id: IdProposal; +name; +status: ProposalStatus; +priority: Natural; +validity: Date} * proposals_sent — 1 municipal_manager Person; Sending * proposals_received — 1 federal_manager Person; ProposalAssessment * reviews — * reviewers Person; Sending {date <= proposal.validity} {«imm» +date: Date = Sismob.today()}; Proposal 1 — * Sending; Sending 1 — * Modification {+text: String = ""}; Sending 1 — * Proposal Assessment {date <= self.sending.proposal.validity} {+concluded: Boolean = FALSE; +text: String = ""; «imm» +date: Date = Sysmob.today()}; Cancellation 0..1 — 1 Proposal; Sending 1 — 0..1 Funds Allocation with Funds Deallocation, Publication, Phase Completion Requisition → Phase Assessment (0..1 each).

Use Case: Decide on proposal (main flow)

1. Federal manager searches for {proposals qualifiedc to receive a «decision» (at least three assessments and before deadline).

2. System presents list of proposals, showing first the ones with {shorter deadlinec.

3. Federal manager selects proposal.

4. System presents proposal name, status, priority, validity, and the {list of assessmentsc attached.

5. Federal manager writes the «motivation» for her decision.

6. System confirms that all {conditions to decidec are ok. [E1]

7. Federal manager approves the «continuation» of the proposal. [V1] [V2]

8. System sends «email» to municipal manager.

Variant V1: Proposal is canceled

V1.1 Federal manager «cancels» the proposal.

V1.2 System sends email to municipal manager.

V1.3 Use case ends.

Variant V2: Proposal needs modifications

V2.1 Federal manager writes a {list of modificationsc needed. [E2]

V2.2 System sends email to municipal manager.

V2.3 Use case ends.

Exception E1: Text of motivation is too «short»

E1.1 System presents message MODAL.482.

E1.2 Use case returns to main flow step 5.

Exception E2: Proposal needs modifications and the list of modifications is empty

E2.1 System presents message MODAL.483. E2.2 Use case returns to step V2.1.

Just as before, first thing is to examine the text of the use case and marking words or expressions that are new candidates to concepts or attributes. To avoid repeating all the text of the use case, it was already done on its first presentation above.

Now, the use case is analyzed and compared with the conceptual model of Fig. 10–3.

In the first line of the main flow, we see that proposals must be qualified by having at least three assessments and being before deadline. Deadline is already an attribute of proposal (validity), but the limit number of three may be represented as a system variable accessible by a method such as Sismob.minimum_assessments(). Thus “qualified for decision” may be a derived attribute of class Proposal. However, when writing the OCL expression, the team may recall that a proposal may have multiple sendings and that the assessments are associated to the sendings and not to the proposal in order to allow many versions of the proposal to be analyzed. If the role from Proposal to Sending is marked with {ordered} «stack», then the most recent proposal can be retrieved by popping the top of the stack, which is the last element added.

The following OCL expression may represent it:

```ocl
Context Proposal::qualified_for_decision:Boolean
    derive:
        self.sending->last().date <= self.validity
        AND self.sending->last().assessments->size()
            >= Sismob.minimum_assessments()
```

To avoid repeating the expression self.sending- . last(), we can define a single identifier to this expression by using the “def”: declaration of OCL:

```ocl
Context Proposal::qualified_for_decision:Boolean
    def: last_sending = self.sending->last()
    derive:
        last_sending.date <= self.validity
        AND last_sending.assessments->size()
            >= Sismob.minimum_assessments()
```

Still in line 1, the federal manager should produce a decision that comes with a text and possibly an enumeration with approved, canceled, and waiting_changes. Those attributes may be represented in class Sending. As a decision is not necessarily made when the federal manager is attached to the sending, then both attributes may be optional («opt»).

Continuing the analysis of the use case, in line 2, it is observed that the proposals are presented sorted by deadline proximity. Actions such as sorting lists may be done by the interface itself, but in this case, just to demonstrate the use of the controller class and a derived association, let us define a role from controller to proposal that consists of a sorted collection.

Thus the controller class may be included in the conceptual model and attached to the independent concepts that in this case are: Person, and? Just Person. All other concepts are dependent on another one. Then, a directed association from Controller to Person is added to the model.

In order to obtain a list of proposals sorted by deadline, we can create a derived association from Controller to Proposal. This association is proposals_by_deadline. We could, at this point, annotate in the CSD matrix a supposition: past deadline proposals are not shown in this list. Thus it must be confirmed later with the client, but now the team may assume it as true. Thus the OCL expression to define that derived association could be:

```ocl
Context Controller::proposals_by_deadline: OrderedSet(Proposal)
    derive:
        self.person.proposals_sent->select(:proposal|
            proposal.validity < Sismob.today()
        )
        ->sortedBy(:proposal|
            proposal.validity
        )->asOrderedSet()
```

The first part of the expression is the filter “select” that returns only proposals for which deadlines are still valid. The function “sortedBy” places the objects in the set into an order that is given by the expression between parenthesis: proposal.validity. As sortedBy returns by default a sequence, we have changed it to be an ordered set by using asOrderedSet().

In line 4, the “list of assessments” of a proposal may contain the assessments related to the last sending. This information can already be obtained in class Proposal by the OCL expression self.sending- . last().

In line 5, motivation is defined as an optional attribute of Sending that goes by the name decision_motivation.

In line 6, conditions to decide are a derived attribute of class Proposal named qualified_for_decision.

In Line 7, the continuation of a sending is represented by the optional attribute final_status in class Sending, which can receive one of the values of the new enumeration DecisionType.

Finally, the email mentioned in line 8 may be one of three kinds of preformatted texts including the decision motivation and final status. It reminds us that a Person, in this system, should have and email to receive communication. The attribute email added to class Person has a primitive type Email that checks its format.

In variant V1, the cancelation event is represented by one of the values of attribute final_status of Sending.

The list of modifications mentioned in variant V2 could be a new optional attribute of Sending, or it can be considered as part of the text already in decision_motivation. It can be marked in the CSD matrix as a supposition that a new attribute is not necessary in this case. The team should opt for the simpler solution, but as this is not a certainty, it should be checked later with the user or client.

Exception E1 mentions the possibility of the motivation text to be too short. The minimum size can be stated in terms of characters and defined as a constant if it is a permanent requirement or as a system variable if it is a transient requirement. As the team does not know the value at this time, it should be marked as a doubt in the CSD matrix and resolved later. As in the case of a sorted list, this verification is purely syntactic, and it could be made by the interface itself. However, if the team prefers to represent it in the conceptual model, they should create a primitive type such as MotivationText that defines the acceptable sizes of this kind of text. Another option, more complicated, would be to create an invariant in class Sending stating that if the decision_motivation has a value, it should be a text with at least a certain number of characters.

Exception E2 mentions that the list of modifications may be empty. Well, this should make the team to revise a supposition from before and establishing the list of modifications as information to be associated to a sending. As it is a multivalued information, it cannot be an attribute of Sending, because we already mentioned that having attributes typed as collections is an antipattern that hinders the cohesion of the class. Thus Modification is added as a new class in the model, and it has a role “– ” from Sending indicating that the “list” of modifications is in fact a set. If it was mentioned that the modifications have some type of priority, maybe that role could be changed to an OrderedSet, but there is no evidence for now that this is necessary. Fig. 10–4 shows the result after all those discoveries.

**Figure 10–4: Conceptual model after analyzing a second use case.** *(p. 176)*

> **Diagram content (transcribed from the figure image):** Final conceptual model of the example: Controller —(one-way) *{ordered} proposals_by_deadline→ Proposal and Controller → * Person; Proposal {«imm» «unique» +id: IdProposal; +name: String; +status: ProposalStatus; +priority: Natural; +validity: Date; +/qualified_for_decision: Boolean}; Proposal * proposals_sent — 1 municipal_manager Person {+id: ID; +name: String; +email: Email}; Proposal 1 — {ordered}«stack» * Sending {date <= proposal.validity} {«imm» +date: Date = Sismob.today(); «opt» +decision_motivation: MotivationText; «opt» +final_status: DecisionType}; Sending * proposals_received — 1 federal_manager Person; Sending 1 assessments — * ProposalAssessment {+/concluded: Boolean = sending->notEmpty()}; ProposalAssessment * assessments — * reviewers Person; Sending 1 — * Modification {+text: String}; Sending 1 — 0..1 FundsAllocation → FundsDeallocation (0..1), Publication (0..1), PhaseCompletionRequisition (0..1) → PhaseAssessment (0..1); Cancellation 0..1 — 1 Proposal; «enumeration» DecisionType {approved, cancelled, waiting_changes}; «enumeration» ProposalStatus {?}; «primitive» MotivationText.

Well, this finishes our presentation of this chapter. The team could continue to analyze other use cases and should continue to refine and complete the conceptual model from this point. As the more complex use cases are really examined before the others, it is expected that in the end of the process very few modifications would be necessary to the model because it would already have all important information. At this point, the team will be reaching a stable architecture, which is one of the conditions to start producing code.

## Questions (Chapter 10)

1. What kinds of words are concepts and attribute candidates in the text of a use case?

2. How to differentiate concepts from attributes in the text of a use case?

3. How to find associations in the text of a use case?

4. What are dependent and independent concepts? Give three examples of each.

5. How to chose which use cases are going to be analyzed first?

This page intentionally left blank

