<!-- Knowledge file: Chapter 6 — Expanded use cases -->
> **About this file.** Chapter 6 of a cleaned, AI-ready edition of Wazlawick, R. S. (2024). Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-443-13739-6.  
> **Covers:** Expanded use cases: main flow, alternate flows (exceptions, variants), writing recommendations, included use cases and fragments, other sections, expansion of stereotyped (CRUD/report) use cases.  
> **Use this file when:** writing detailed use case specifications (scenarios, main and alternate flows, preconditions, business rules).  
> **Sections:** 6.1 Introduction to expanded use cases (p. 87); 6.2 Main flow (p. 90); 6.3 Alternate flows (p. 91); 6.4 Writing recommendations (p. 95); 6.5 Included use cases and fragments (p. 99); 6.6 Other sections of an expanded use case (p. 100); 6.7 Expansion of stereotyped use cases (p. 101); 1.2 Variant flows (p. 102); 1.3 Excep–on Flows (p. 103); 1.4 NF-CRU.01 – Non-Func–onal Requirements for Create and Update (p. 104); 1.5 NF-CRU.02 – Non-func–onal requirements for Dele–on (p. 105); 1.6 NF-CRU.03 – Non-func–onal Requirements for Retrieve (p. 105); 1.7 NF-CRU.04 – Non-func–onal Requirements for Lis–ng (p. 106)  
> **Contains:** 0 figures transcribed as text, 0 code listings.

# Chapter 6: Expanded use cases

*Source: Wazlawick, Object-Oriented Analysis and Design for Information Systems, 2nd ed. (Elsevier, 2024), starts p. 87*

## Key topics in this chapter (Chapter 6)

- Main flow of a use case

- Alternate flows: exception handlers and variants

- Use case fragments

- Writing recommendations

- Essential and real use cases

## 6.1 Introduction to expanded use cases

*Chapter 6 · p. 87*

As seen before, use cases may be used to represent system requirements, among other things. They are useful for requirements because they allow the building of a structure that is easy to understand, communicate, and manage. They allow the representation of the system processes and actors in different levels of abstraction. Ivar Jacobson identifies some reasons why use cases are so useful:^1

- A use case model is a picture that allows a team to describe even a complex system. It tells in simple terms what the system is going to do for its users.

- A use case produces value to a particular user, not to an unidentifiable community of them.

- Use cases are also test cases; when the team finishes organizing requirements in use cases, they have also produced the structure needed for test cases.

- Use cases are the starting point to design effective user experiences or stories.

- Use cases drive development from analysis to design, from design to code, and from code to testing.

In the beginning of a sprint, the team performs a Sprint Planning Meeting, which consists, among other things, in choosing the user stories or use cases from the Product Backlog accordingly to their priority and the capacity of the team.

The next task is to find scenarios inside the more complex use cases, which could be a way to divide the more complex use cases into manageable fragments. Here, there is an agile principle that states that the tasks allocated to a sprint should not be too big neither too small. From the point of view of XP, the ideal task must have from one to three story points, while the PMBOK^2 accepts 1–10 story points or 8–80 hours. Thus the team must evaluate

> *Footnote 1:* http://blog.ivarjacobson.com/use-cases-%E2%80%93-why-successful-and-popular/.

> *Footnote 2:* https://www.pmi.org/pmbok-guide-standards/foundational/pmbok.

89 each use case in the beginning of the sprint and decide which ones will be single tasks (for being of the size acceptable by the team) and which ones should be divided into fragments to be more manageable during the sprint.

Notice that use cases do not have to be divided into technical tasks such as analysis, design, implementation, and test. What the team must do is to find different scenarios inside the main story. The most common scenarios are the variants and exception handlers, which are explained in this chapter. To find those fragments, the team needs to expand the use case and find its main flow of transactions, as explained bellow.

To proceed with the expansion of a given high-level use case, it could be useful to have at hand the system use case diagram, including all annotations or not functional requirements, and the supplementary specifications document. It would also be useful, for the first iteration, to have a version of the preliminary conceptual model. The team may use the conceptual model to help expand use cases, and at the same time, the expanded use cases would provide information to refine the conceptual model that after the first sprint is not “preliminary” any more, but “under refinement.”

As use case expansion corresponds to the refinement of the functional requirements, the team must conduct a very detailed exam on the process incorporated into the use case from the point of view of the user. It would be very useful if the user is present when the team is discussing the use case expansion because the user is the best people to describe a list of tasks, variants, and exceptions that happens in her working journey.

In a first approach, the use case should be essential because in the beginning of analysis, the team may have no idea of its future interface. For this activity, the presence of the user is essential! After the essential flows are discovered, the team may propose one or more possible designs for the system interface. In this case, the team would appreciate if at least one competent designer is a member.

After deciding on the best proposal for the interface, the team may annotate the text of the use case and identify each action in the use case with one or more components of the interface. In this case, the use case evolved from essential to real or concrete.

## 6.2 Main flow

*Chapter 6 · p. 90*

The main flow is the most important section of an expanded use case. It is the description of the use case process when everything goes right, that is, when no alternate flow occurs.

In the SISMOB example, a first draft of the main flow of the use case “Produce proposal assessment” could be something like this:

Use case: Produce proposal assessment

1. Reviewer search for process.

2. System presents list of processes allocated to reviewer, newest first.

3. Reviewer selects process.

4. System presents process name, status, priority, and validity.

5. Reviewer registers assessment and conclusion.

6. System confirms operation.

This is what is expected if everything goes well during the use case flow. But problems may arise. For example, for each business rule, there must be an exception handler, and variations of the main flow may exist.

As it can be seen, there is a pattern that repeats like:

1. The user informs. . .

2. The system informs. . .

Each pair of this kind is considered as a transaction and corresponds to the user taking some action followed by a reply by the system. The first transaction in the use case “Produce proposal assessment” is composed of steps 1 and 2, where the user asks for a list of projects and the system presents the projects that this reviewer has access.

The second transaction is composed of steps 3 and 4, where the user selects a project to work from the list provided by the system, and the system responds by showing some information on the selected process.

The third and final transaction is when the user writes an assessment about the project and concludes the operation what is responded by the system simply by confirmation that the data were received.

Observe that this is an essential use case. Thus information about user interface should not exist. There are no mentions to buttons, windows, menus, etc. It is not mentioned also by what kind of interface the information is passed or received. Most developers could be assuming keyboard, mouse, and screen. However, other options could be proposed, tested, and selected when it is time to propose and choose a good user interface. Later!

A use case flow is, therefore, a sequence of transactions. It is not an algorithm with loops and decision points. It is a straight line of events. Alternate flows are defined outside the main flow.

## 6.3 Alternate flows

*Chapter 6 · p. 91*

A use case specifies a process that can be performed in real life in several different ways. In the last example, two people producing assessments would maybe take different sequences of steps. If the sequences are sufficiently similar^3 , then the same flow must be used to describe both.

But in some situations, alternate flows must be used to indicate sequences that could occur in quite different ways.

> *Footnote 3:* For example, one customer writes two lines and another customer writes fifteen lines: both actions may be described simply as “reviewer writes assessment” because the number of lines is irrelevant for understanding the process.

There are basically two kinds of alternate flows: variants, which indicate different ways to reach the same goal, and exception handlers, which indicate how to deal with obstacles to the flowing of the process.

### 6.3.1 Scenarios — 6.3 Alternate flows

A use case can be understood as a description or general specification that supports a set of different scenarios. Each scenario is a particular realization or instance of the use case. Usually, a use case has a main scenario (execution of the main flow) and alternate scenarios (executions of the main flow that pass by one or more alternate flows). However, the notion of main flow variants sometimes creates doubt on what should really be a use case. In the “Produce proposal assessment” example, considering that the process for writing an assessment may be long (even taking some days sometimes), we can consider that the use case has at least two finalizations:

- A reviewer writes a partially completed assessment and save it to continue another time (use case ends and could start again latter).

- A reviewer may write or not new information in the saved assessment and sends it to the system as a final decision (use case ends for good).

Is it a single use case with two alternative ends? Or should it be split into two use cases, one that ends with saving only and one that ends with sending a saved assessment?

Both options are equally valid, although one of them is possibly more useful than the other. The choices are:

- Create more use cases (one for each scenario). Each use case has a simpler structure, but there would be a high number of similar use cases. For example, one use case to write an assessment and another use case to send it as a final decision.

- Group similar scenarios in a single use case. There are a smaller number of use cases, but each of them would be more complex. For example, there is only one use case for writing an assessment and it can be finished by saving or by sending.

At this point, it is more important to discover the information exchanged between the actors and the system than to decide if two scenarios consist of one or two use cases. The team should evaluate and decide on the simpler solution. Moreover, one of the main goals here is to discover which is the user usual journey, and which transactions she must perform during this journey. It does not matter so much if the transactions belong to a single use case or to a pair of use cases; what is important here is to discover that they exist.

However, the advantage of joining alternate scenarios into a single use case is that the description of some steps must not be repeated in different use cases.

### 6.3.2 Variants — 6.3 Alternate flows

It is admitted, in principle, that the main flow of a use case is a strict sequence of transactions: it is neither branched nor nested.

A use case with two different endings such as “Produce proposal assessment” may have one scenario that is more typical (not necessarily more common, but it should be the natural path that comes to mind when someone describes the use case). In this case, the typical path is to write and assessment and send it as final. Deciding on continuing it another time could be considered as a variant.

Variants are not represented in use case as branches. The main flow is kept as a linear set of steps and the variants are referenced after the main flow. In our example, the “Produce proposal assessment” we should perceive that step 5 may not include sending the assessment. Then a variant can be defined for this step.

Use case: Produce proposal assessment (main flow)

1. Reviewer searches for process.

2. System presents list of processes allocated to reviewer, newest first.

3. Reviewer selects process.

4. System presents process name, status, priority, and validity.

5. Reviewer registers assessment and conclusion. [V1]

6. System confirms operation.

Variant V1: User decides to save for continuing latter

V1.1 Reviewer registers assessment and saves it.

V1.2 System confirms that the assessment is saved.

V1.3 Use case ends.

Saving the text to resume it later is not an exception (such as an obstacle) but an option for the user. That is not a condition that prevents the use case from concluding, because the use case still produces something: the assessment is saved and can be resumed later. One way to number variants is by using the letter “V” and a sequence of numbers, such as V1, V2. If a variant such as “V1” occurs only in one or a few steps, then it can be noted in the main flow, by using a label such as “[V1].” If the variant may occur in any step of the use case, it does not need to be referenced in the main flow.

### 6.3.3 Exception handling — 6.3 Alternate flows

After describing the main flow of a use case and adding variants (if any), the team can concentrate on identifying the exceptions that could occur and create an alternate flow for each one. Each business rule annotated for a use case will usually generate an exception. For example, if the use case for producing assessments has a business rule that states that the assessment must be send not later than 30 days after the proposal is received, trying to do that will be an exception. At this point, the team may consult the user about what can be done (or if something can be done) to surpass this exception and finalize the use case. In this example, when the deadline is closed without an assessment being sent, this reviewer cannot change or send it anymore. The process would have been probably already assigned to another reviewer at this time. Therefore this is a kind of exception that prevents the use case to be concluded with success. It fails because the user cannot reach the business goal.

In other cases, things could be different. For example, the user may insert a wrong password. The exception handler in this case usually provides another trial (maximum three, usually) and the “forget my password” option, which is almost universal nowadays in systems that demand passwords. If you get your password right on the second or third times, the use case may continue; if you recover your password, the use case may continue too. It means that the exception was handled. But, if you fail at the third try, you would be blocked by the system and probably a more complex process would be needed to recover your password.

The example below corresponds to the final form of the use case “Produce proposal assessment” with all variants and exceptions found by the team in the real case of SISMOB.

Use case: Produce proposal assessment (main flow)

1. Reviewer searches for process.

2. System presents list of processes allocated to reviewer, newest first.

3. Reviewer selects process.

4. System presents process name, status, priority, and validity.

5. Reviewer registers assessment and conclusion. [V1]

6. System confirms operation.

Variant V1: User decides to save for continuing latter.

V1.1 Reviewer registers assessment and saves it. V1.2 System confirms that the assessment is saved. V1.3 Use case ends.

Exception E1: Deadline reached BR-FNS.01^4 .

E1.1 System presents message MODAL.114^5 . E1.2 User acknowledges. E1.3 Use case fails.

Exception E2: Proposal was not prioritized BR-FNS.06.

E2.1 System presents message MODAL.371.

> *Footnote 4:* BR-FNS.01 is a reference to the Business Rule (BR) that may be observed here and that is catalogued with the other business rules of the system.

> *Footnote 5:* MODAL.114 is a reference to the message shown by a modal window that is catalogued with the other messages of the system. A modal window blocks navigation until the user acknowledges having read it.

E2.2 User acknowledges. E2.3 Use case fails.

Like variants, exceptions are numbered by using the letter “E,” and a numerical sequence.

Steps in alternate flows may use the code of the alternate flow as part of the number, such as “E1.1,” or they may be numbered simply by a sequence 1, 2, 3, etc.

Each alternate flow must indicate if the use case ends with success, or if it fails, as in the example. Beyond success and fail, other possibility is to return to some step in the main flow after concluding the alternate flow. One good example of this case is when you are buying something on the Internet, and you have changed your address since the last buy. Changing address in the system does not belong to the main flow. It is a variant that consists of informing a new address and then returning to the main flow of the use case to conclude payment and anything else.

## 6.4 Writing recommendations

*Chapter 6 · p. 95*

The writing style of a use case should follow a pattern such as “actor informs. . ./system informs. . ..” Styles such as “system asks. . .” should be avoided because what must be represented in the use case is the flow of information, not the occasional demands that gave rise to those flows; those demands do not exist in every scenario, and in most of them they are not even necessary.

The team must avoid placing tests in the use case main flow. Tests such as “if the user has a record, then the system presents. . .” should be avoided. That kind of test is unnecessary because exception handlers should already be associated to the steps of the main flow. Then, if an exception occurs, it would be handled in an alternate flow.

These tests must not be placed in the main flow to keep it from becoming a complex flowchart instead of a straight, simple sequence of transactions. Lots of “if/then” statements can make the flow obscure, and the stakeholder would not know what the expected flow (happy path) is.

Another common writing concern is that a use case must alternate inputs and outputs of information (transactions). In other words, normally a use case has the form “actor informs . . ., system informs . . ., actor informs . . ., system informs . . ..”

Sequences such as “actor informs . . ., actor informs . . ., actor informs . . .” or “system informs . . ., system informs . . ., system informs . . .” must be avoided.

The idea behind the alternating pattern is to reduce any discrepancy on the number of steps that different analysts could assign to the same use case. Without that rule, one analyst could write:

The customer provides name, ID^6 , and phone number.

6 Here and in further examples in this book, the ID provided by a customer is not a system-generated internal code, but the number of a personal document that belongs to the customer. In the United States, the social security number could correspond to the ID number, while in other countries, other numbers could be used.

On the other hand, another analyst could write:

1. The customer provides name.

2. The customer provides ID.

3. The customer provides phone number.

The most useful and correct version under this point of view is the first, because, among other things, the second would demand that the information be provided in the order of the steps: after providing the ID, the user cannot go back and correct her name. Thus the first version is more compatible with most information systems, which present interfaces where information in many fields may be entered and edited before it is finally sent to the system.

### 6.4.1 Essential versus real use case — 6.4 Writing recommendations

A frequent doubt about use cases is which system must be described? The current one? Or the one that will be built? If the current operations are performed manually, and in the future, they will be performed with a computer, what must be the description provided by the use case? The answer is none, but both! The use case written for analysis purposes must describe the essence of the operations, not their concrete realization. Thus the analyst should always try to avoid mentioning the technology used to perform the process and concentrate only on the exchanged information. Instead of writing “the clerk writes the customer’s name and address on a paper sheet,” corresponding to a manual technology used normally in nonautomated systems, or “the customer fills in the name and address on fields F1 and F2 on the main screen,” which corresponds to an automated technology, the analyst must register the operation simply as “the customer provides name and address.” The last form is technology-free and interface-independent and represents, therefore, an essential description for the operation.

All use cases used for requirements purposes should be, in principle, essential. Essential in this context means that the use case is described in a language where only the essence of the operations is presented, not its concrete counterpart. In other words, the analyst must describe “what” happens between the user and the system without informing “how” that interaction happens. The analyst should not, therefore, while doing analysis, try to describe the interface technology between the user and system. This will be described during design time in which real use cases could be written after the real interface has been designed. Real use cases stay attached to a specific interface technology, while essential use cases are technology-free.

Why essential use cases? According to Ambler (2004), real use cases (those that mention technology) contain too many built-in assumptions, often hidden or implicit about the underlying technology of interface implementation strategies. That may be a good feature during design, but not during requirements analysis. An essential use case, on the other hand, states the user needs or intentions, and not the concrete technology that could support those needs.

As the description of the use case at that moment is made without reference to the interface technology, it is not necessary to decide what the interfaces look like, but only what information is exchanged between actors and system. References to menus, windows, buttons, and other graphical devices should be avoided in the text of the essential use cases.

So how do we describe use cases that seem to be particularly concrete such as drawing money from an automatic teller machine? How do we do that without describing technology? It is possible. Instead of saying “the user inserts a magnetic card,” one could say that “the user provides identification.” Instead of saying that the machine “prints the account details,” one could say that the machine “presents the account details.” Thus by eliminating the reference to the physical technology, only the essence remains. This opens the way for the design of innovative technologies later, that is, interfaces different than those that can be seen at a first glance. For example, the user could be identified by fingerprints, the receipt could be sent by SMS (Short Message Service), and even the money could be delivered in cash or in credits to a preloaded card.

It is the responsibility of the team to study the current processes of the company and produce an essential version of them in the form of essential use cases. Later, the team will give a new form to those processes by using technology to produce a new concrete version of the system. At this step, different proposals may be at stake, and some of them would be prototyped and tested before one is chosen.

### 6.4.2 Explicit information — 6.4 Writing recommendations

For the sake of understanding use cases as functional requirements, it is recommended that the analyst makes explicit the individual data pieces exchanged between actors and the system. Thus instead of a laconic “customer provides data,” the use case should say “customer provides name, ID, email, phone, and address.”

Eventually, a term such as “customer” could be externally defined as meaning “name, ID, email, phone and address.” An expression such as customer 5 , name, id, email, phone, address. could be written in documentation. If that definition is adequately registered, for example, in the conceptual model, or in a data dictionary, then it can be used in the use case text to avoid repeating the individual elements every time they have to be mentioned.

### 6.4.3 Identification and selection — 6.4 Writing recommendations

A recurrent problem associated to use cases is how to identify people and things. For example, a reviewer must be identified and validated in order to perform the “Produce proposal assessment” use case. How does she do it? Username and password? Social security number? Fingerprints? Selecting the name from a predefined list or menu? To keep the use case essential, that particular action must be left generic, and references to possible ways for identifying a reviewer must be left to design. Furthermore, the computer security community already has established common methods to securely validate an identity, and these proven methods should be used instead of reinventing the wheel. For now, the use case could simply state that the user provides identification, without mentioning by which means that identification is obtained and validated.

Another example is the selection of a project for analyzing. Does the reviewer submit the number of the project? Select it from a list? Use a natural language speech interface? During use case expansion, these issues do not need to be decided (unless they are indeed nonfunctional or supplementary requirements). At the essential level of the use case, the user simply selects a project. Later, the design will present some options to provide the means for the user to make that selection in the most comfortable way.

### 6.4.4 Mandatory, complementary, and unsuitable steps — 6.4 Writing recommendations

What steps are mandatory in an expanded use case? Are there some that are optional? In fact, two people that describe the same use case, unless they have a nicely established convention, may produce different flows with different steps.

In any scenario of a use case, the mandatory steps are those that cannot be suppressed without leaving the flow impossible to perform in terms of information changing between user and system. An assessment cannot be completed if a project is not selected, for example.

However, other steps that could be included may not be so important. If an analyst writes, “for example, that the system asks for an information,” that step could be removed from the sequence and the flow could still make sense, given that in any case the user provides that information, with or without being asked to.

Analysts must be encouraged to build correct versions of the use cases, but they should not stop there: they may produce the smallest use case possible, by including only mandatory steps and avoiding optional ones.

Mandatory steps include information that is passed from the actors to the system and from the system to the actors. Without one of those steps, the flow may not make sense.

Other steps such as “ask for information” or “send confirmation message” are optional or complementary. They may help contextualize the use case, especially the real ones. But they are not fundamental because they do not transmit any information through the system boundary.

In a use case description, the information can not appear from nowhere. It is transmitted from the actors to the system and vice versa. The absence of any mandatory step may make the use case seem incomplete because information that is needed by the system is not sent by the user or vice versa.

Later, the information contained in the mandatory steps of a use cases could be used to refine the conceptual model.

Depending on the direction the information goes, mandatory steps may be identified as:

- System events: Steps that indicate that some information is transmitted from the actors to the system.

- System returns: Steps that indicate that some information is transmitted from the system to the actors.

Special care must be taken when considering system returns. For those steps to be mandatory, they must pass some information that the system stores or can access externally in other systems. That information must be something that in principle the actors do not have access to, except by querying the system.

Complementary steps are not fundamental in essential use cases because they do not correspond to system events or system returns, as they do not transmit information through the system boundary.

Some of them can be even mapped to navigation operations during interface design. For example, a real use case (design) could have a step like such as “the user opens window W32.” That line does not correspond to a system event because at that time, the customer does not pass any information to the system (such as name, phone, address, and book title, etc.). That action corresponds simply to a change of state that will be implemented as interface navigation (a new screen is opened after the option is selected, for example).

The team must also keep in mind that, as the use case is a description of the interaction between actors and system, they must avoid including internal system processes, such as “the system stores the information into the database..” Those steps are considered unsuitable for the essential use case description. Considering the real version of the use case, those steps could be included if the internal process is not obvious. For example, every time a record is inserted or updated, there is a change in the database, and it must not be written in any version of the use case. However, if some exceptional internal operation happens, such as activating a thread for searching some information, it could be represented associated with a mandatory step.

The use case is a tool for describing the interaction between users and a system, not a tool to describe internal processing. The internal processes of the system will be better described during design with more adequate tools.

## 6.5 Included use cases and fragments

*Chapter 6 · p. 99*

It is possible for two or more use cases to have coincident parts. For example, many use cases may include an identification fragment. In other cases, a use case may include not only a fragment, but a complete use case, such as for example, a payment. The “include” relationship should be used only when the duplicated fragment or use case is significant, that is, it should not be used when just one step is duplicated. An included use case or fragment may be called in a flow by using the “include ,fragment or use case name . ” expression.

Some care must be taken here. First of all, use cases are not procedures like the ones used in programming languages; they are linear descriptions of real-world processes. Teams are not encouraged to structure use cases as they do with code. Included use cases or fragments may be used only when the situation really justifies it.

However, the analyst must keep in mind that the goal of the expanded use case in analysis is to help in understanding the nature of the interactions between the system and its actors, and not to structure a computer program to simulate that interaction. Thus, the included use case or fragment calls must be used carefully.

## 6.6 Other sections of an expanded use case

*Chapter 6 · p. 100*

Since the concept of a use case was created (Jacobson et al., 1992), different formats have been proposed. Each proposal includes different elements. The “main flow” and “alternate flows” sections are fundamental for any fully dressed use case description. However, other sections can be included if the team needs them. Some of the most popular are presented in the next subsections.

### 6.6.1 Stakeholders — 6.6 Other sections of an expanded use case

There are often scenarios where groups other than actors are relevant to a use case. Other sectors of the organization could have some interest in the use case. For example, in the use case “Register proposal,” the only actor is the Municipal Manager. But the results of that use case may interest other stakeholders, such as, for example, the law department of the municipality and the financial department, which may be interested in knowing if the proposal is adequate to the laws and finances of the municipality. Thus, even if those departments are not participants in the use case, they can be listed as stakeholders. And they may also be a source of requirements.

The utility of the stakeholders list for a use case is that the use case must satisfy all stakeholders. Thus, the documentation will be useful to remind the team to seek information that needs to be stored, processed, or transmitted, so that those interests can be satisfied.

### 6.6.2 Preconditions — 6.6 Other sections of an expanded use case

Preconditions are facts assumed true before a use case starts. Preconditions must not be confused with exceptions: exceptions may be detected only after the use case has started. Exceptions are detected during a use case because most of the time it is not possible to verify if the conditions were true or not before the use case begins. For example, it is not possible to assure that the project has enough funds to be executed before starting the use case that sends the project to the National Health Fund; therefore, this is an exception. However, it is possible to admit that the user that sent the proposal is registered in the system. Thus assuming that the user is registered may be considered as a precondition.

As preconditions are accepted as true facts before the use case starts, they would not need to be checked during the use case flows, except if concurrent operation may turn the precondition invalid.

### 6.6.3 Success postconditions — 6.6 Other sections of an expanded use case

Success postconditions establish the results of a use case, that is, what will be true after the use case is executed. For example, the “Send proposal” use case may have as a postcondition the following result: “the proposal was received by the federal manager.”

### 6.6.4 Open issues — 6.6 Other sections of an expanded use case

Sometimes, without the presence of the client or user, the team cannot decide about some issue that may depend on company policies. For example, may a project be sent with annexes? Is there a time limit between creating a new proposal and sending it?

If the client is not immediately available, these doubts must be recorded in the use case section “open issues” to be solved as soon as possible.

Other tool that can be used for this purpose is the CSD (Certainties, Suppositions, and Doubts) matrix. It can be a single matrix for the entire product, and it has three columns: the first states what the team knows for certain (former doubts or suppositions that were resolved by the client or user, and must not be asked again), the second is for suppositions, that is, issues that the team assume to be true, but that must be confirmed, and the third for doubts, that is, issues that the team has no idea how to deal with. The matrix is used to register doubts and suppositions and as soon as they are resolved, they must be moved to the first column where they stay to remind the team that they were once a doubt or supposition but was already confirmed.

At the end of the analysis activities of one sprint, it is expected that all open issues have been resolved and incorporated into the use case description.

## 6.7 Expansion of stereotyped use cases

*Chapter 6 · p. 101*

Stereotyped or pattern use cases usually present low risk to the software development process because the structure of their flows and many business rules are already known. The most common pattern is identified by the ,, CRUDL . . stereotype. If it is adequately documented, it may pass to the team a clear idea of what must be implemented for each of its instances.

Chart 6–1 is the documentation of the final version of every CRUDL use case in the SISMOB project. It was adapted from the SISMOB final documentation.

In the case of CRUDLs what can be said is that not every entity of the conceptual model is suitable to be managed by the CRUDL pattern. CRUDLs are expected to be the simplest entities. If they get more complex, a set of non-CRUDL use cases will be necessary for describing how the user works with them.

For instance, a user and an assessment are very simple entities and could be nicely managed by a CRUDL use case. On the opposite side, a proposal is one of the most complex entities of the SISMOB system. Proposals may be issued, canceled, completed, sent, resent, received back, etc. That does not characterize it as a CRUDL.

In the gray zone, there are concepts that the team must look at to decide if they may be adequately managed as a CRUDL or not. For example, is “Managing funds allocation” a CRUDL or not? Some time may be spent on analysis before the team can decide on that.

#### 1. UC-CRU.01 – CRUDL – Real version

Represents the basic opera–ons of CRUDL - Create, Retrieve, <mark>Update,</mark> Delete, and List.

Precondi–ons: The user is iden–fied and authen–cated. Access to the modules and their opera–ons must be validated by access control as described in RN-AUT.02 - Access Control and must be consistent with the standardiza–on of the system.

#### 1.1. Main Flows

The CRUDL stereotype has four main flows, one for each of the CRUD opera–ons. Lis–ng is considered not to be a flow, but the default star–ng page of this group of use cases.

#### Create - Basic Path

1. <mark>The</mark> actor selects the op–on to create a register.

2. The system presents the registra–on screen with the save and cancel op–ons.

3. The actor fills in the required informa–on and selects the save op–on [V1].

4. The system validates the informa–on, saves the record, displays the default success message, and returns to the screen before the registra–on [E1].

#### Update - Basic Path

1. The actor selects the op–on to update.

2. The <mark>system</mark> presents the registra–on screen with the op–ons save, cancel, and delete.

3. The actor fills in the required informa–on and saves [V1].

4. The system validates the informa–on, saves the record, displays the default success message, and returns to the screen before edi–ng the registra–on [E1].

#### Dele–on - Basic Path

1. The actor selects the delete op–on.

2. The system displays the confirma–on message MODAL.003.

3. The actor confirms the dele–on.

4. The <mark>system</mark> deletes the record, displays the default success message, and returns to the screen before the record was deleted.

#### Retrieve - Basic Path

1. The actor selects the op–on to retrieve data.

2. The system <mark>presents</mark> the preview screen with the edit and delete op–ons.

3. The use case is finalized.

## 1.2 Variant flows

*Chapter 6 · p. 102*

#### V1: Cancel Create/Update – Variant

1. The actor selects the cancel op–on.

2. The system displays the default cancel <mark>confrma–on</mark> i message.

3. The actor confirms the cancella–on.

4. The system discards the registered informa–on and returns to the screen before the registra–on.

CHART 6–1 SISMOB CRUDL use case pattern.

## 1.3 Excep–on Flows

*Chapter 6 · p. 103*

#### E1: Invalid informa–on and/or mandatory fields – Excep–on

1. The system does not validate the informa–on and displays the valida–on message.

2. The <mark>actor</mark> closes the valida–on message.

3. The system returns to step 3 of the main flow.

#### E2: Func–onality or registry not available – Excep–on

1. The actor selects some system op–on, and the registry is no longer available, or the <mark>func–onality</mark> can no longer be performed.

2. The system displays the error message MSG.359.

#### E3: No permission to access the registry - Excep–on

1. The actor selects some system op–on, and the user is not allowed access to the <mark>registry</mark> or func–onality.

2. The system displays the error message MSG.179.

#### E4: Unexpected error – Excep–on

1. The actor selects some system op–on, and an <mark>unexpected</mark> error (ERROR_MSG) occurs.

2. The system displays the error message MSG.405.

#### E5: Database connec–on error – Excep–on

1. The actor selects some system op–on, and the connec–on to the database has been lost

- ( <mark>CONNECTION_ERROR_MSG)</mark> or is invalid (ILEGAL_ERROR_MSG).

2. The system displays the error message MSG.406.

#### E6: Syntax or database structure error – Excep–on

1. The actor selects some system op–on, and an error <mark>occurs</mark> due to syntax failure, or the database structure is incompa–ble (SQLSYNTAX_ERROR_MSG).

2. The system displays the error message MSG.407

#### E7: Null mandatory informa–on error – Excep–on

1. The actor selects some system op–on, and the query or <mark>opera–on</mark> does not return a required informa–on to con–nue (NULLPOINTER_ERROR_MSG).

2. The system displays the error message MSG.407

#### E8: Server out of memory – Excep–on

1. The actor selects some system op–on, and an error occurs due to lack of memory on <mark>the</mark> applica–on server (OUTOFMEMORY_ERROR_MSG).

2. The system displays the error message MSG.407

#### CHART 6–1 Continued.

## 1.4 NF-CRU.01 – Non-Func–onal Requirements for Create and Update

*Chapter 6 · p. 104*

**1.** The opera–ons of “Create”“and “Update must be validated by access control according to BR-AUT.02 Access Control and must follow the standardiza–ons defined in System Standardiza–on.

**2.** The business rules and requirements are described in <mark>each</mark> module.

**3.** When selec–ng the “Create” op–on, the system should show the <mark>“Create”</mark> screen.

**4.** When selec–ng the “Update” op–on, the system should show the Create screen with the informa–on of the selected record.

**5.** When selec–ng the “Save” op–on a–er edi–ng a record, the system should display <mark>the</mark> message MODAL.094.

**6.** When trying to cancel or exit a new registra–on, if it has any informa–on registered, it should show the message MODAL.001.

**7.** When trying to cancel or exit the upda–ng or crea–on of a record where it is possible to save without finishing, if it has any informa–on changed, it should show the message MODAL.002.

**8.** If any data from the registra–on is filled out/selected in a previous screen (pre- <mark>selec–on</mark> ), this data should be considered as registered informa–on.

**9.** The above messages must be in accordance <mark>with</mark> the module op–on (save, send, or confirm) and, if the op–on is to send, the finish message must be used.

**10.** Required fields must be validated and, if necessary, show the MSG.011 in error-type <mark>no–f</mark> i <mark>ca–on</mark> mode and an errortype hint for each field with the MSG.010 message.

**11.** The values of the fields must be validated and, if an invalid value field exists, show the MSG.007 in error-type no–fica–on mode and an error-type hint for each field with the MSG.006 message.

**12.** For mandatory fields and fields with invalid <mark>values</mark> in the same valida–on, it should show the MSG.012 message in error-type no–fica–on mode while retaining the aforemen–oned hints for each field. For free typing text fields, the valida–on of the maximum number of characters must be performed. If the user exceeds the maximum limit set in the data dic–onary, the system must prevent the inser–on of more characters.

**13.** When a record is successfully saved, the system should <mark>display</mark> the MSG.001 in success no–fica–on mode.

**14.** If the page refreshes and unsaved data is lost, it should display the message MSG.264.

**15.** A record cannot be changed by more than one <mark>user</mark> simultaneously. Thus, when a–emp–ng to edit a record and it is being edited by another user, the system should display the MSG.048 message in alert-type no–fica–on mode.

#### Breadcrumbs:

The descrip–on to be used in breadcrumb should be:

#### _> Insert/edit [name of en–ty]_

Example: “Insert/edit proposal”, “Insert/edit User”

CHART 6–1 Continued.

## 1.5 NF-CRU.02 – Non-func–onal requirements for Dele–on

*Chapter 6 · p. 105*

**1.** The “Delete” opera–on must be validated by access control as described in RN-AUT.02 - Access Control.

**2.** Business rules and requirements are defined in each module.

**3.** When a–emp–ng to delete a record, the system should display the MODAL.003 confirma–on message.

**4.** If the registry dele–on is successful, it should display the MSG.031 message in success no–fica–on mode.

**5.** Dele–ng records should be logical, changing the record status to “Inac–ve”.

**6.** A record cannot be deleted when it is being edited by another user.

**7.** When a–emp–ng to delete a record and it is being edited by another user, the system should display the MSG.048 message in alert-type no–fica–on mode.

## 1.6 NF-CRU.03 – Non-func–onal Requirements for Retrieve

*Chapter 6 · p. 105*

1. Access to the modules and their visualiza–on must be validated by access control as <mark>described</mark> in RN-AUT.02 Access Control.

2. When selec–ng the “Preview” op–on, the system should show the preview screen with the data from the <mark>selected</mark> record and, where allowed the “Update” and “Delete” op–ons.

3. No changes to the registra–on are allowed through this op–on.

#### Breadcrumbs:

The descrip–on to be used in <mark>breadcrumb</mark> should be:

**_> Informa–on about [name of en–ty]_**

Examples: “Informa–on about user”, “Informa–on about proposal”

CHART 6–1 Continued.

## 1.7 NF-CRU.04 – Non-func–onal Requirements for Lis–ng

*Chapter 6 · p. 106*

**1.** Access to lis–ngs must be validated by access control as described in RN-AUT.02 - Access Control.

**2.** Business rules and requirements are defined in each module.

#### Filters:

**3.** The screen must display the “Clear Filters” <mark>op–on.</mark>

**4.** When selec–ng the “Clear Filters” op–on the system should clear all filter fields and update the lis–ng.

**5.** The lis–ng should be automa–cally updated with each filter fill or selec–on.

#### Column sor–ng:

**6.** If the list has columns with the op–on to sort, the selected column will be sorted in an ascending or decreasing manner according to the actor's need.

#### Select all items:

**7.** If the lis–ng has the selec–on op–on, the system must present an "All" op–on at the top of the list so that all items are selected.

**8.** By clicking the op–on:

-

-

- If the items in the list are not selected, the system must check all items.

- If the items are already checked, the system must deselect all items.

#### Empty list:

**9.** If there is no data to be displayed in the lis–ng, the system must display the message MSG.049.

**10.** For more details see RI-COM.03 - Lis–ngs.

#### Op–ons:

**11.** The op–ons available in the lis–ngs are described in <mark>each</mark> module and should be consistent with the RN-AUT.02 Access Control

#### Breadcrumbs:

The <mark>descrip–on</mark> to be used in breadcrumb should be:

**_> List of [name of en–ty in the plural]_**

Examples: “List of users”, “List of Proposals”

CHART 6–1 Continued.

## Questions (Chapter 6)

1. Variants and exception handlers are alternate flows for a use case. In which situations should one or the other be used?

2. What is the difference between an essential use case and a real use case? Why is the essential use case more interesting for requirements purposes?

3. Explain the differences between mandatory, complementary, and unsuitable use case steps.

4. What are preconditions for a use case?

5. Think or search for other examples of use case patterns, that is, general forms of use case, such as CRUDL, that can be defined generally and instantiated many times in different projects.

This page intentionally left blank

7

