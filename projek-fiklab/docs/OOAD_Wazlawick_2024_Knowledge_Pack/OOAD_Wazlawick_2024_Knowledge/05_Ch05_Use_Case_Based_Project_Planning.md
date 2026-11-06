<!-- Knowledge file: Chapter 5 — Use case-based project planning -->
> **About this file.** Chapter 5 of a cleaned, AI-ready edition of Wazlawick, R. S. (2024). Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-443-13739-6.  
> **Covers:** Effort estimation (ad hoc, parametric, use case/story points, technical and environmental factors), linear time, sprint duration, use case priority, project monitoring.  
> **Use this file when:** estimating effort with use case points, planning sprints, prioritizing use cases or monitoring project pace.  
> **Sections:** 5.1 Introduction to effort estimation (p. 64); 5.2 Ad hoc techniques (p. 64); 5.3 Parametric techniques (p. 66); 5.4 User story points (p. 67); 5.5 Linear time (p. 77); 5.6 Estimating the duration of the sprints (p. 83); 5.7 Defining use case priority (p. 84); 5.8 Monitoring a project (p. 85)  
> **Contains:** 6 figures transcribed as text, 0 code listings.

# Chapter 5: Use case-based project planning

*Source: Wazlawick, Object-Oriented Analysis and Design for Information Systems, 2nd ed. (Elsevier, 2024), starts p. 64*

Key topics in this chapter

- Effort Estimation

- Risk Assessment

- Ideal and Minimum Development Times

- Prioritizing Use Cases

## 5.1 Introduction to effort estimation

*Chapter 5 · p. 64*

The motivation for effort estimation in software projects comes from the fact that historically most software development projects:

- Take more time to complete than expected.

- Cost much more than expected.

- Generate a product that does not have the quality expected.

- Generate a product that does not have the scope expected.

Thus the point is that software development teams and clients must learn to expect the right time, cost, quality, and scope regarding their project. Effort estimation techniques are used to accomplish these goals.

Effort estimation may be divided into two big groups: parametric and nonparametric. In the following subsections, both will be presented and discussed.

## 5.2 Ad hoc techniques

*Chapter 5 · p. 64*

Several techniques for effort estimation have been proposed and used in the last several decades. One that is very popular is the Smith technique, which may be summarized as “Smith, tell us how much time you need to develop that system!” A variation of the Smith technique is the Constrained Smith, which may be summarized as “Smith, you have three months to develop that system!.” Although popular (and known by other names, such as Susan, Peter, Mary, etc.), this approach may not be very accurate and depends strongly on the person experience on estimating software effort.

Another ad-hoc technique that is used is the Six Months technique. It consists of estimating “six months” for any software project at the beginning of its negotiation with the client and then adjusting it up or down as the real scope and requirements are discovered. 

65

Variations of that technique are virtually infinite, including the One Year technique and the Eighteen Months technique, among others.

Somerville (2006) identifies some other ad hoc techniques:

- Expert judgment. The expert judgment technique proposes that one or more experts on the project domain and software development should meet and use their experience to produce an estimate. The Smith technique is a potentially bad scenario for the expert judgment technique: the technique may be very inaccurate, depending on the expertise of the estimators. However, if the experts really have wide experience in similar projects, it is a feasible, quick, and relatively effortless technique.

- Estimation by analogy. That technique is in fact the pragmatic basis for the expert judgment technique. It is assumed that the effort for developing a new system will be like the effort for developing other similar systems. The technique is not feasible if similar projects are not available for comparison. It can make good use of one or more experts to determine what qualifies as a similar system and how the time spent to develop it may be used as a basis to estimate the effort for the current project. Thus this technique usually may evolve to expert judgment.

- Parkinson’s Law. That technique is not usually adopted openly, but it is recurrent in software projects and in other areas: the project costs whatever resources are available. The advantage is that the project will not cost more than expected, but eventually the scope of the system will not be completely covered. This technique is explained by the dialog: “How much will the system cost?” answered by the question “How much do you have?.”

- Pricing to win. The cost of the project is equal to the price that is believed to win the contract. The disadvantage of this method is that the system the client gets may not be what she expected, because as costs must usually be reduced, this may impact on quality and scope.

These kinds of techniques are known as nonparametric estimation because they are not based on measures on the project to be developed.

## 5.3 Parametric techniques

*Chapter 5 · p. 66*

Another class of estimation techniques includes the parametric ones, which aim to present an effort estimation based on the estimated size of the system, the technical difficulty to develop it, and the capacity of the team, among other features. The size of the system may be measured in terms of:

- Lines of code. Techniques such as COCOMO II—COnstructive COst MOdel II (Boehm, 2000) start estimating how many source lines of code the system will have. In fact, as most systems have thousands of lines of code, the usual measure is kilo source lines of code (KSLOC).

- Function points. Techniques based on function point analysis (FPA) (Albrecht, 1979) and its variations are not concerned about lines of code. They estimate that the effort to develop a system depends on the apparent functionality that is going to be implemented. Thus usually these techniques count the number of functional requirements and evaluate their complexity by asking about how many elements and functions the interfaces have and about the number and size of database tables.

- Use case points. That is a variation of the FPA technique that is based on use cases instead of functional requirements for estimation.

Although COCOMO II is the most detailed technique, it has a disadvantage compared with function points and use case points: the number of KSLOC must be estimated by specialists before applying the method, and this is a significant source of uncertainty.^1 In the end, COCOMO II is like a variation of specialist opinion with a lot of technical adjustments made based on statistics about real projects. However, the first kick problem remains: will the system have 20K, 30K, or 70K lines of code?

## 5.4 User story points

*Chapter 5 · p. 67*

The agile community usually adopts an estimation strategy that is based on story points. As we discussed before, a user story is a scenario of use of a system, and it is somewhat like a use case. However, use cases are more structured and formal; they are produced by a team of analysts. User stories, on the other hand, must be written by the users themselves. They must represent a scenario where the users see themselves using the system that is going to be produced. The idea behind this is that the users present the needs that are most important for them first; the details would be recalled later.

This book measures the size of use cases with story points, because a use case can be in fact the evolution of a user story.

One story point is one ideal working day (6–8 hours focused and dedicated to a project). The estimation effort is then calculated for each user story or use case in terms of story points. The question to be answered by the team is, “How many ideal days x people would take to develop a given user story?” If the answer is x people would take y days, then the number of story points is x 3 y. Story points assignment is subjective, and this is why it is considered a nonparametric technique.

### 5.4.1 Two ways to estimate story points — 5.4 User story points

We have seen that the Bridge Laboratory uses an estimation technique that is a variation of user expert. The difference is that the expert does not estimate alone, the estimation is made together with one or more agile teams. The agile teams are free to use the estimation technique they prefer given that they deliver the result in story points. Two of those techniques are presented in the following subsections.

> *Footnote 1:* To minimize this uncertainty, backfire tables that convert function points into KSLOC may be used for some classes of systems (Boehm, 2000).

### 5.4.1.1 Selecting from the whole set of stories — 5.4 User story points

When this technique is used, all histories (or use cases) have their names written in stickers and placed on a table or a wall where all the team may see them. The first step of the algorithm is to remove the stories or use cases considered to be feasible by one developer in less than one day, that is, a user story or use case with less than one story point. Those stories are left separated for being joined later with one of themselves or another related but more complex story.

The second step is to remove stories that are feasible in more or less one day by one developer. Those stories are attributed one story point and will be separated from the other more complex stories that remain in the table or wall.

The third step, you may have guessed yet, is to separate user stories with two story points and make a new group with them. This algorithm proceeds by separating stories that are similar in size until no story is left on the table or wall.

However, the increasing scale used is not the natural numbers, but a kind of rounded Fibonacci numbers, as seen in Table 5–1.

The team may use other scales, such as 1, 2, 4, 8, 16, . . .. The important thing is that they understand that the idea here is not to hit the value but to identify which stories are similar in terms of effort to be developed. This idea is based on the fact that a human usually does not know how much an adult horse weighs, but she knows that it weighs more than a dog and less than an elephant.

### 5.4.1.2 Planning poker — 5.4 User story points

Another way to estimate the effort for a user story or use case is to give each team member a set of cards representing the numbers in the rounded Fibonacci scale and voting. The voting process happens as follows: one user story or use case is selected from the stack or list and presented and discussed by the team. Then, each team member places one card on the table with the number hidden to the other members. When all have placed their cards, they are all open. If they agreed more or less, for example, 3, 5, 3, 3, 3, 2, 3, their rounded average is assigned as their user points; in the example: 3. If one or more disagree a lot, for example, 3, 2, 3, 20, 3, 5, 2, where the “20” is far from the average of the other numbers, then the member that disagreed must explain why she has done so, and the team will discuss if the reasons are valid or not. Then a second round is done and values more similar are expected.

**Table 5–1: Natural, Fibonacci, and rounded Fibonacci numbers.**

|Natural|1|2|3|4|5|6|7|8|9|10|11|12|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Fibonacci|1|2|3|5|8|13|21|34|55|89|144|233|
|Rounded Fibonacci|1|2|3|5|10|15|20|35|50|90|150|250|

If the disagreement happens again, the team may discuss and vote again. Continuing the discussion after a second round may be frustrating and useless. Then, if a quasi-agreement is not obtained, the number of user points may be calculated as:

where UP is the number of user points assigned to the user story or use case, Wmax is the value of the maximum guess by the team, Wmin is the value of the minimum guess by the team, and Waverage is the average of the other guesses by the team.

### 5.4.2 What to consider when estimating story points — 5.4 User story points

The team usually evaluates the effort of a system component based on their experience on similar past projects. The assignment is made based on effort, complexity, and risk:

- Effort: How many lines of code or function points must be considered?

- Complexity: How difficult is to analyze, implement, and test the component?

- Risk: How much does the team understand the component?

In the following subsections, we will discuss those criteria in more detail.

### 5.4.2.1 Effort — 5.4 User story points

Effort may be associated with the “brute force” involved in programming. In the case of user stories, the length of the story and the quantity of scenario variations may be a clue to estimate the user story effort.

In the case of use cases, usually the team must estimate or develop the detailed version of the use case to know how many transactions it has. A transaction is a pair of input and output to and from the system. For example, if a user requires the balance of her account and the system informs the value, that was a complete transaction. If, after that the user asks to withdraw some money and receives the money, that was a second complete transaction.

Karner initially proposed the t-shirt^2 scale for use cases:

- Use cases with up to three transactions are small.

- Use cases with four to seven transactions are medium.

- Use cases with more than seven transactions are large.

However, Karner did not show how to convert those values into developing time, such as story points. Thus we suggest that the team should use the estimated number of transactions together with complexity and risk for helping to decide on the number of story points of the use case.

2 Sizes: small, medium, and large.

### 5.4.2.2 Complexity — 5.4 User story points

Complexity is related to the difficulty to analyze, implement, and test the story or use case. The Use Case Point Technique of Karner adapted the Technical Complexity Factor from Function Points technique and introduced a new set of Environmental Complexity Factors that were later adapted to the Function Point Technique too.

We can use the technical complexity factors to understand the complexity of the component and the environmental complexity factors to understand its risks.

Each factor receives a rating from 0 to 5, where 0 means no influence on the project, 2.5 is nominal influence, and 5 is maximum influence on the project.

There are 13 technical factors, each one with a specific weight, as shown in Table 5–2.

Tables 5.3–5.17 show the interpretation of each of those complexity factors and how the rank should be assigned.

For the Function Points and Use Case Points Analysis those ranks would be used to reach a value that would be used in the calculations to produce a number known as “Adjusted Function/Use Case Points” that number is used to calculate the time to develop the system by multiplying it by the productivity index of the team. However, here we are not making this conversion so fast.

Those thirteen complexity factors usually apply to the system as a whole, but looking at the parts of the system, we can see that they are not usually homogeneous. For example, one use case may demand high-level security, but others do not. Thus the team can use this tables as a reference to analyze the relative complexity of each part of the system.

Table 5–16 shows an example of a comparative table with some use cases belonging to the same application being analyzed individually. The last row is the average that allows to compare use cases among them in terms of complexity. Ranks closer to 0 mean easy use cases, ranks closer to 5 means very complex use cases and 2.5 is the nominal or average complexity use case.

**Table 5–2: Technical factors used by function points estimation technique.**

|Factor|Description|Weight|
|---|---|---|
|T1|Distributed system|2.0|
|T2|Response time/performance objectives|1.0|
|T3|End-user efficiency|1.0|
|T4|Internal processing complexity|1.0|
|T5|Code reusability|1.0|
|T6|Easy to install|0.5|
|T7|Easy to use|0.5|
|T8|Portability to other platforms|2.0|
|T9|System maintenance|1.0|
|T10|Concurrent/parallel processing|1.0|
|T11|Security features|1.0|
|T12|Access for third parties|1.0|
|T13|End user training|1.0|

#### Table 5–3 Distributed system.

Is the system architecture centralized or distributed?

|Rank Scenario|
|---|

- 0 The application ignores any aspect related to distributed processing.

- 1 The application generates data that will be processed by other computers with human intervention (e.g., spreadsheets or preformatted files sent by media or email).

- 2 Application data are prepared and transferred automatically for processing in other computers.

- 3 Application processing is distributed, and data are transferred in just one direction. 4 Application processing is distributed, and data are transferred in both directions.

- 5 Application processes must be executed in the most appropriate processing core or computer, which is dynamically determined.

#### Table 5–4 Response time/performance objectives.

What is the importance of the application response time to its users?

|Rank Scenario|
|---|

- 0 No special performance requirement was defined by the client.

- 1 Performance requirements were established and revised, but no special action must be taken. 2 Response time and transfer rates are critical during peak hours. No special design for processor core use is necessary. The deadline for most processes is the next day.

- 3 Response time and transfer rates are critical during commercial hours. No special design for processor core use is necessary. Requirements regarding deadlines for communication with interfaced systems are restrictive.

- 4 In addition to 3, performance requirements are sufficiently restrictive for requiring performance analysis tasks during design.

- 5 In addition to 4, performance analysis tools must be used during design, development, and/or implementation, in order to meet the client’s performance requirements.

In this table, we considered that UC1 is a mathematical related module, with less human interaction, but high internal processing. UC2 is a user-oriented module with less internal complexity but a lot of user specific resources. UC3 is a module that deals with sensitive data and demands special security but has no other important features.

The averages resulting indicate that UC1 and UC2 have similar complexity while UC3 is relatively simpler.

### 5.4.2.3 Risk — 5.4 User story points

The last important factor that determines the relative size of a use case or user story is risk. Risks are variable and volatile, and many risks tables can be found in literature. In this book we decided to work with risks in order to calculate effort in developing and thus it seemed natural to use the environmental complexity factors of use case points in order to help understanding relative use case sizes based on risks.

#### Table 5–5 End-user efficiency.

Is the application designed to allow final users just to do their job or is it designed to improve their efficiency?

Rank Scenario

- 0 The application does not need any of the items below.

- 1 The application needs one to three of the items below.

- 2 The application needs four to five of the items below.

- 3 The application needs six or more of the items below, but there is no requirement related to user efficiency.

- 4 The application needs six or more of the items below, and the user efficiency requirements are so strong that the design must include features to minimize typing, maximize defaults, use templates, etc.

- 5 The application needs six or more of the items below, and the user efficiency requirements are so strong that the design activities must include tools and special processes to demonstrate that the performance goals are obtained.

The following items must be considered for the assessment of the end-user efficiency item:

- Navigational help (e.g., dynamically generated menus and adaptive hypermedia).

- Online help and documentation.

- Automated cursor movement.

- Predefined function keys.

- Batch tasks submitted from online transactions.

- High use of colors and visual highlights in screens.

- Minimizing the number of screens to reach the business goals.

- Bilingual support (counts as four items).

- Multilingual support (counts as six items).

#### Table 5–6 Internal processing complexity.

Does the application need complex algorithms?

|Rank|Scenario|
|---|---|
|0|None of the options below.|
|1|One of the options below.|
|2|Two of the options below.|
|3|Three of the options below.|
|4|Four of the options below.|
|5|All five options below.|

The following options need to be considered for assessing internal processing complexity:

- Careful control (e.g., special audit processing) and/or secure processing specific to the application.

- Extensive logical processing.

- Extensive mathematical processing.

- Lots of exception processing resulting from incomplete transactions that needs to be reprocessed, such as incomplete automated teller machine transactions caused by interruption of communication, missing data values, or failed data change.

- Complex processing to manage multiple inputs and output possibilities, such as multimedia or device independency.

#### Table 5–7 Design aiming for code reusability.

Is the application designed so that its code and artifacts will be highly reusable?

- Rank Scenario 0 There is no concern about producing reusable code.

- 1 Reusable code is generated for use inside the same project. 2 Less than 10% of the application must consider more than the user needs. 3 10% or more of the application must consider more than the user needs. 4 The application must be specifically packaged and/or documented for facilitating reuse, and the application must be customizable by the user at the level of source code.

- 5 The application must be specifically packaged and/or documented for facilitating reuse, and the application must be customizable by the user with the use of parameters.

#### Table 5–8 Easy to install.

- Will the application be designed so that its installation is automatic (e.g., in the case of users with low or unknown technical capacity), or is there no special concern about it? Rank Scenario 0 The client established no special consideration, and no special setup is necessary for installation. 1 The client established no special consideration, but a special setup is required for installation.

- 2 The client established requirements for data conversion and installation, and conversion and installation guides must be provided and tested. The impact of conversion in the project is not considered important.

- 3 The client established requirements for data conversion and installation, and conversion and installation guides must be provided and tested. The impact of conversion on the project is considerable.

- 4 In addition to 2, tools for automatic conversion and installation must be provided and tested. 5 In addition to 3, tools for automatic conversion and installation must be provided and tested.

There are eight environmental factors that assess the working environment. Each one has its own weight and two of them have negative weights. Again, ratings range from 0 to 5, but their meaning is a little different from those of the ratings attributed to the technical factors. While the ratings of the technical factors evaluate the influence of those factors on the project, the ratings of the environmental factors evaluate the quality of those factors in the working environment. For example, a 0 rating for the “motivation” factor means that the team is not motivated, a 2 or 3 rating means that motivation is about average, and a 5 rating means that the team is highly motivated. The environmental factors are defined in Table 5–17.

Ribu (2001) presents a reference for assigning ratings to the environmental factors, which is described in Tables 5–18 to 5–25 with some adaptation.

Those environment factors are applied to a team, not to parts of the system. However, as a project may have many teams, their respective risks can be calculated individually. Then, the risk associated to the team may be associated to the use cases they are developing in case of an estimation.

#### Table 5–9 Easy to operate^3 .

- Are there special requirements regarding the operation of the system? Rank Scenario 0 No special considerations about the operation of the system besides normal backup procedures were established by the user.

- 1 One of the items below applies to the system. 2 Two of the items below apply to the system. 3 Three of the items below apply to the system. 4 Four of the items below apply to the system. 5 The application is designed to operate in nonsupervised manner. “Nonsupervised” means that human intervention is not necessary for keeping the system operational, even if crashes occur, except maybe for the first startup and final turn off. One of the application features is automatic error recovery.

- For the evaluation of the easy to operate factor, the following items must be considered: • Effective processes for initialization, backup, and recovery must be provided, but operator intervention is still necessary. • Effective processes for initialization, backup, and recovery must be provided, and no operator intervention is necessary (counts as two items).

- The application must minimize the need for data store in offline media (e.g., tapes).

- The application must minimize the need for dealing with paper.

#### Table 5–10 Portability.

- Is the application or parts of it designed to work on more than one platform? Rank Scenario 0 There is no user requirement to consider the need for installing the application in more than one platform. 1 The design must consider the need for the system to operate in different platforms, but the application must be designed to operate only in identical hardware and software environments.

- 2 The design must consider the need for the system to operate in different platforms, but the application must be designed to operate only in similar hardware and software environments.

- 3 The design must consider the need for the system to operate in different platforms, but the application must be designed to operate in heterogeneous hardware and software environments.

- 4 In addition to 1 or 2, a documentation and maintenance plan must be elaborated and tested to support operation in multiple platforms.

- 5 In addition to 3, a documentation and maintenance plan must be elaborated and tested to support operation in multiple platforms.

Let’s, for example, consider two teams. Team 1 is a group of five professionals recently graduated in Computer Science that studied object-oriented techniques, but without significant professional experience. Three of them are fully dedicated to the project, while the other

3 Occasionally, this item is referred to as “usability,” but the original concept of usability was already considered in factor T3, “end-user efficiency.” We prefer to interpret this factor as “easy to operate” to avoid confusion and redundancy with the end-user efficiency factor.

**Table 5–11: Design aiming for easy maintenance.**

Does the client require that the application must be easy to change in future?

|Rank|Scenario|
|---|---|
|0|None of the items below.|
|1|One of the items below.|
|2|Two of the items below.|
|3|Three of the items below.|
|4|Four of the items below.|
|5|Five or more of the items below.|

To evaluate this factor, the following items are considered:

- A flexible report structure must be provided to deal with simple queries such as logical binary operators applied to just one logical archive (count as one item).

- A flexible report structure must be provided to deal with medium complexity queries such as logical binary operators applied to more than one logical archive (count as two items).

- A flexible report structure must be provided to deal with high complexity queries such as combinations of logical binary operators applied to one or more logical archives (count as three items).

- Business control data are kept in tables managed by the user with interactive online access, but changes must only be effective on the next day (count as one item).

Business control data are kept in tables managed by the user with interactive online access, and changes are effective immediately (count as two items).

#### Table 5–12 Concurrent/parallel processing.

Must the application be designed in order to deal with problems related to concurrency such as data and resource sharing? Rank Scenario

- 0 No concurrent access to data is expected. 1 Concurrent access to data is expected sometimes. 2 Concurrent access to data is expected frequently. 3 Concurrent access to data is expected all the time.

- 4 In addition to 3, the user indicates that a lot of multiple accesses are going to happen, forcing performance analysis tasks and deadlock resolution during design.

- 5 In addition to 4, the design requires the use of special tools to control access.

two have other activities. This will be the first project they are going to work professionally together. Despite having little experience in software industry, they are highly motivated, and their lead analyst has a little more than 1 year of experience as such.

On the other hand, Team 2 is a dream team as they have experienced people (more than 3 years) in Scrum, object-oriented processes, knowledge of application, and programming language. The team is highly motivated, and all workers are full-time. The different ranks for teams 1 and 2 are shown in Table 5–26.

#### Table 5–13 Security.

Are the security needs just nominal or are a special design and additional specifications required?

|Rank|Scenario|
|---|---|
|0|There are no special requirements regarding security.|
|1|The need for security must be taken into account in design.|
|2|In addition to 1, the application must be designed so that it can be accessed only by authorized users.|
|3|In addition to 2, access to the system will be controlled and audited.|
|4|In addition to 3, a security plan must be elaborated and tested to support access control to the application.|
|5|In addition to 4, a security plan must be elaborated and tested to support auditory.|

#### Table 5–14 Access to/for third-party code.

Is the application going to use code already developed, such as commercial off-the-shelf (COTS) components, frameworks or libraries? High reuse of good quality software reduces the value of this item as it implies less development effort.

- Rank Scenario 0 Highly reliable preexistent code will be used extensively for developing the application. 1 Highly reliable preexistent code will be used in small parts of the application. 2 Preexistent code that eventually needs to be adjusted will be used extensively for developing the application. 3 Preexistent code that eventually needs to be adjusted will be used in small parts of the application. 4 Preexistent code that needs to be fixed or is hard to understand will be used in the application. 5 No preexistent code will be used in the application or questionable quality code will be used in the application.

#### Table 5–15 User training needs.

Will the application be easy to use, or must extensive training be given to future users?

|Rank|Scenario|
|---|---|
|0|There are no specific requirements for user training.|
|1|Specific user training requirements have been mentioned.|

- 2 There are formal specific user training requirements, and the application must be designed to facilitate training. 3 There are formal specific user training requirements, and the application must be designed to support users with different levels of training.

- 4 A detailed training plan must be elaborated for the transition phase and executed. 5 In addition to 4, the users are geographically distributed.

The difference between the two teams shows that the first team may face a lot of problems if they start a nontrivial project without trying to improve some of their ranks. On the other side, the dream team may face the project risks with more competence. In the end, Team 1 would take much longer to develop the same project as Team 2, and that may be reflected to every use case assigned to them.

**Table 5–16: Some use cases and their complexity comparison.**

|Factor|Description|Weight|UC1|UC2|UC3|
|---|---|---|---|---|---|
|T1|Distributed system|2.0|0|0|3|
|T2|Response time/performance objectives|1.0|3|4|2|
|T3|End-user efficiency|1.0|2|5|1|
|T4|Internal processing complexity|1.0|5|1|2|
|T5|Code reusability|1.0|3|2|2|
|T6|Easy to install|0.5|0|5|0|
|T7|Easy to use|0.5|1|5|1|
|T8|Portability to other platforms|2.0|0|0|0|
|T9|System maintenance|1.0|3|3|3|
|T10|Concurrent/parallel processing|1.0|5|2|0|
|T11|Security features|1.0|2|2|5|
|T12|Access for third parties|1.0|4|0|5|
|T13|End user training|1.0|1|5|4|
||Weighted average||2.03|2.07|1.75|

**Table 5–17: Environmental complexity factors.**

|Factor|Description|Weight|
|---|---|---|
|E1|Familiarity with development process used|1.5|
|E2|Application experience|0.5|
|E3|Object-oriented experience of team|1.0|
|E4|Lead analysis capability|0.5|
|E5|Motivation of the Team|1.0|
|E6|Stability of Requirements|2.0|
|E7|Part-time staff|21.0|
|E8|Difficulty with programming language|21.0|

## 5.5 Linear time

*Chapter 5 · p. 77*

There are many ways to address the issue of the linear or calendar time to run a project. One is based on the number of agile teams available. As we know the size of each team, we know how many story points each team can develop each working day. We also know the number of story points attributed to each product of the project that is the sum of the story points of each use case or user story. Then, it would be possible to allocate each team to different products until all products are allocated. As the teams can work in parallel, they can use the same calendar days to perform their work.

For example, consider a project with seven products, the size of which (number of story points) is depicted in Table 5–27.

Then, we can allocate products to the three agile teams considering if they are idle or not.

**Table 5–18: Familiarity with the development process used^4 .**

|This facto|r assesses the team’s experience with the development process they are using.|
|---|---|
|Rank|Scenario|
|0|The team does not have experience with the development process or does not use any process.|
|1|The team has theoretical knowledge about the development process, but no experience.|
|2|A few members of the team have already used the process in one project.|
|3|A few members of the team have used the process in more than one project.|
|4|Up to half the team has used the process in many projects.|
|5|More than half the team has used the process in many projects.|

**Table 5–19: Experience in the application.**

|This facto applicatio|r assesses the familiarity of the team with the application area or domain. For example, if the n is about e-commerce, have the team already worked with systems in the same area?|
|---|---|
|Rank|Scenario|
|0|No team member has any experience in projects in the same area.|
|1|Some team members have 6–12 months of experience in projects in the same area.|
|2|Some team members have 12–18 months of experience in projects in the same area.|
|3|Some team members have 18–24 months of experience in projects in the same area.|
|4|Most team members have 18–24 months of experience in the same area.|
|5|Most team members have more than 24 months of experience in the same area.|

The agile teams may have different sizes. Thus let’s consider that Team 1 has five members, Team 2 has seven members, and Team 3 has four members (Table 5–28). Each time we allocate a team in the calendar (this calendar considers only working days, not holydays), we allocate a number of days that is the number of story points of the project divided by the size of the team.

First, we allocate project P1 with 220 story points to Team 1 that has five members. So, we must allocate 220/5 5 44 working days. Then, we allocate P2 to Team 2. As P2 has 630 story points and Team 2 has seven members, we should allocate 630/7 5 90 working days. Then, Team 3 with four members will have allocated P3 with 400 story points. Thus we allocate 400/4 5 100 working days. Notice that even if P3 has less effort than P2, it takes more time because the team is smaller. The linear time each team would use to develop each product is depicted in Table 5–29.

The results up to now may be seen in Fig. 5–1.

We see then that the first team to terminate a product is Team 1. Thus they can take over P4. As P4 has 240 story points and Team 1 five members, we should allocate 240/5 5 48 working days. As Fig. 5–2 shows, the next team to terminate a product is Team 2. We

> *Footnote 4:* Originally the factor mentioned the Unified Process, and some authors even mention UML here. But this has been adjusted to reflect the fact that other processes and modeling languages could be used instead.

**Table 5–20: Object-oriented experience of the team.**

This factor must not be confused with either familiarity with the development process (E1) or experience in the application (E2): this is about the experience of the team in doing object-oriented analysis, modeling, design, and programming, independently of the application area and the development process used.

|Rank|Scenario|
|---|---|
|0|No team member has any experience in projects in object-oriented techniques.|
|1|Some team members have 6–12 months of experience in object-oriented techniques.|
|2|Some team members have 12–18 months of experience in object-oriented techniques.|
|3|Some team members have 18–24 months of experience in object-oriented techniques.|
|4|Most team members have 18–24 months of experience in object-oriented techniques.|
|5|Most team members have more than 24 months of experience in object-oriented techniques.|

**Table 5–21: Lead analyst experience.**

This factor measures the experience of the lead analyst with requirement analysis and object-oriented modeling, that is, typical analysis tasks.

|Rank|Scenario|
|---|---|
|0|The lead analyst has no experience.|
|1|The lead analyst has up to 6 months of experience.|
|2|The lead analyst has 6–12 months of experience.|
|3|The lead analyst has 12–18 months of experience.|
|4|The lead analyst has 18–24 months of experience.|
|5|The lead analyst has more than 2 years of experience.|

allocate P5 to them: 80/7 5 11.5 D 12 working days (we should probably always “round” up in these cases).

As the process continues, we allocate P6 to Team 1 with 120/5 5 24 working days and P7 to Team 3 with 70/4 5 17.5 D 18 working days. The final allocation is depicted in Fig. 5–3.

Notice that if teams with different sizes would have been used, the allocation could be very different from this one. Notice also that if we have allocated P7 or P6 to Team 2 and P5 to Team 3 or Team 1, we could finish all the project a couple of days earlier. This can be considered before deciding on the final allocation (unless you need Team 2 to be free before the others, of course). But, considering the allocation of Fig. 5–3 we have:

- P1 starts at day 1 and finishes at day 44.

- P2 starts at day 1 and finishes at day 90.

- P3 starts at day 1 and finishes at day 100.

- P4 starts at day 45 and finishes at day 45 1 48 – 1 5 92

- P5 starts at day 91 and finishes at day 91 1 12 – 1 5 102

- P6 starts at day 93 and finishes at day 93 1 24 – 1 5 116

- P7 starts at day 101 and finished at day 101 1 18 – 1 5 118

#### Table 5–22 Motivation of the team^5 .

|This f|actor describes the team’s motivation.|
|---|---|
|Rank|Scenario|
|0|The team is not motivated at all. Without constant supervision the team becomes unproductive. The team only does what is strictly asked.|
|1|The team has very little motivation. Constant supervision is necessary to keep productivity at acceptable levels.|
|2|The team has little motivation. Management interventions are necessary from time to time to maintain productivity.|
|3|The team has some motivation. Usually the team has initiative, but management intervention is still necessary sporadically to keep productivity.|
|4|The team is well motivated. The team is self-managed usually, but the existence of supervision is still necessary because productivity can be lost without it.|
|5|The team is highly motivated. Even without supervision everyone knows what has to be done, and pace is maintained indefinitely. The team is proactive and addresses almost all problems by themselves.|

#### Table 5–23 Stability of requirements.

This factor evaluates if the team has been able to keep requirements stable in past projects, minimizing their change during the project. This factor may vary from project to project, and from client to client, because there are domains where requirements change often independently of the capacity of the analysts.

- Rank Scenario 0 There is no historic data about requirement stability or, in the past, poor analysis caused big changes in requirements after the project started.

- 1 Requirements were predominantly unstable in the past. Clients asked for many changes caused mainly by incomplete or incorrect requirements.

- 2 Requirements were unstable in the past. Clients asked for some changes caused by incomplete or incorrect requirements.

- 3 Requirements were relatively stable in the past. Clients asked for changes in secondary functionalities with some regularity. Changes to main functionalities were seldomly asked.

- 4 Requirements were mostly stable in the past. Users asked for little changes, especially cosmetic ones. Changes in main or secondary functionalities were unusual.

- 5 Requirements were practically stable in the past. Little changes, if any, had no impact on projects.

Here, we can see that the project as a whole takes 118 days and that P3 and P7 assigned to Team 3 belong to the critical path, meaning that if they are delayed, the whole project is delayed. The other projects have some space to delays: 2 days for Team 1 and 16 days for Team 2.

In the example above, we allocate projects to teams without considering any special features. But that could be the case. For example, just one of the teams may be specialized in

> *Footnote 5:* Surely that is one of the hardest environmental factors to assess, because the real motivation of the team may be masked. Ribu’s (2001) suggestion seemed to help very little in rating this factor, and we took the liberty of reinterpreting the reference.

**Table 5–24: Part-time workers.**

This is a negative factor, that is, contrary to the first six environmental factors, higher values here represent more risk, not less. A team with many members involved in other projects or activities tend to be less productive than a dedicated team.

|Rank|Scenario|
|---|---|
|0|No team member is part time on the project.|
|1|Up to 10% of the team is part time.|
|2|Up to 20% of the team is part time.|
|3|Up to 40% of the team is part time.|
|4|Up to 60% of the team is part time.|
|5|More than 60% of the team is part time.|

#### Table 5–25 Difficulty with programming language.

This is another negative factor, meaning that high values here are bad for the development time. It measures the experience of the team with the language to be used in the project.

|Rank|Scenario|
|---|---|
|0|Most team members have more than 24 moths of experience with the programming language.|
|1|Most team members have 18–24 months of experience with the programming language.|
|2|Some team members have 18–24 months of experience with the programming language.|
|3|Some team members have 12–18 months of experience with the programming language.|
|4|Some team members have 6–12 months of experience with the programming language.|
|5|Team members have up to 6 months of experience with the programming language.|

**Table 5–26: Ranks for two different teams.**

|Factor|Description|Weight|Team 1|Team 2|
|---|---|---|---|---|
|E1|Familiarity with development process used|1.5|1|5|
|E2|Application experience|0.5|0|5|
|E3|Object-oriented experience of team|1.0|3|5|
|E4|Lead analysis capability|0.5|3|5|
|E5|Motivation of the team|1.0|4|5|
|E6|Stability of requirements|2.0|0|5|
|E7|Part-time staff|21.0|3|0|
|E8|Difficult programming language|21.0|4|0|
||Average ranks||0.30|5.00|

mobile applications. If that kind of issue exists, it must be considered when the project is being planned.

We have allocated random products to random teams without worrying about team size or product size. But what if we allocated the bigger product to the smaller team and they

**Table 5–27: Seven products and their story points.**

|Product|Story points|
|---|---|
|P1|220|
|P2|630|
|P3|400|
|P4|240|
|P5|80|
|P6|120|
|P7|70|
|TOTAL|1760|

**Table 5–28: Teams size.**

|Team|#Members|
|---|---|
|1|5|
|2|7|
|3|4|

**Table 5–29: Linear time for each team to develop each project.**

|Product|Story points|Team|#Members|Linear time|
|---|---|---|---|---|
|P1|220|1|5|44|
|P2|630|2|7|90|
|P3|400|3|4|100|
|P4|240|1|5|48|
|P5|80|2|7|12|
|P6|120|1|5|24|
|P7|70|3|4|18|

take much more time than the other teams to complete the product, delaying so the project? That would not be good for sure. For example, if we allocate P2 (630 story point) to Team 3 (four members), they would take 630/4 5 158 working days to conclude P2 and the project would be delayed considering that it could be concluded in 118 days with the previous allocation that we found.

Other important issue is that projects cannot be accelerated indefinitely. If a team with two people can do it in 4 weeks, it does not mean that a team with eight people can do it in one week, neither that 16 people could do it in half a week.

Although there are formulae that dictate the ideal relation between total effort and linear time, their application in practice is very relative. First, they do not work for small projects and second, depending on the type of the project, the numbers would be very different. We suggest here that the team should use common sense and experience to decide if a project can be done with the number of people allocated. Unless you work with projects that last for less than 1 or 2 months, agile teams with less than 10 members usually would do the work in time.

**Figure 5–1: Three products assigned to three different teams.** *(p. 83)*

> **Diagram content (transcribed from the figure image):** Gantt-like allocation: Team 1 does P1 (days 0–~43), Team 2 does P2 (0–~90), Team 3 does P3 (0–~100).

**Figure 5–2: Four projects assigned to three teams.** *(p. 83)*

> **Diagram content (transcribed from the figure image):** Same allocation after Team 1 finishes P1 and takes P4 (~44–~93); Team 2 P2 (0–~90); Team 3 P3 (0–~100).

**Figure 5–3: All seven projects assigned to three teams.** *(p. 83)*

> **Diagram content (transcribed from the figure image):** Full schedule to ~120 days: Team 1: P1 → P4 → P6 (ends ~113); Team 2: P2 → P5 (ends ~100); Team 3: P3 → P7 (ends ~117). Teams pick the next backlog item as they become free.

In any case, always allocate bigger project to bigger teams and smaller projects to smaller teams.

## 5.6 Estimating the duration of the sprints

*Chapter 5 · p. 83*

An sprint begins with planning and finishes with a new version of the system being released internally and/or delivered to the client. The duration of a sprint in Scrum and most agile methods usually ranges from 1 to 8 weeks,^6 and it depends, among other factors, on the complexity of the project and the size of the team.

> *Footnote 6:* Agile methods prefer the shortest duration possible. Some methods such as XP are more radical by forbidding iterations with more than 3 weeks, but other methods are more relaxed on that.

Our experience in the Bridge Laboratory was to initiate with 4-week sprints and after a couple of years of experience changing to 2-week sprints aiming to finally reach 1-week sprints. Nowadays, about half the agile teams work with one and the other half with 2-week sprints.

## 5.7 Defining use case priority

*Chapter 5 · p. 84*

One of the main techniques for reducing risk in a project is dealing first with the most complex use cases, especially if they are those that represent the most critical business processes, because with them the team may learn more about the system than with other use cases. Pattern use cases such as CRUDL (medium complexity) and reports (smallest complexity) can be addressed later.

Planning meetings at the beginning of the sprint may indicate which use cases are going to be analyzed, designed, and implemented.

When planning a sprint, the following aspects must be considered when choosing which use cases to address:

- Use case complexity: Use cases of higher risk and complexity or less understood should be addressed first in most cases.

- Dependencies among use cases: Use cases that have a strong dependence to the ones that were already accommodated in the iteration should be addressed together, if possible, because it avoids fragmenting the work on the classes.

- Team load capacity: The development work must be assigned to team members based on their capacity in story points (number of members 3 number of days of the sprint).

The order of this list is most critical for the complex use cases because a wrong choice in terms of their priorities could lead to otherwise unnecessary refactoring in subsequent iterations. However, the order of use cases with lower risk such as CRUDLs and reports is not so critical.

Have in mind also that use cases are not the only elements that would be allocated to a sprint. If this is not the first sprint, the user would have already asked for some modifications in the system, and they take time to be done and this time must be allocated to the team. Also, project risks that are of high expositions should be treated, and sometimes they need several days to be analyzed and dealt with.

Then, for each element (use case, risk, or change requested), there must be effort estimation or allocation. Estimating effort to develop or change use cases usually is more feasible that estimating time to mitigate a risk. Thus usually a risk has time allocated to it instead of estimated. For example, the team allocates 2 days for three members to mitigate the risk and at the end of this schedule analyzes if the risk was mitigated or not. If not, they decide if it is worthy to start a new mitigation cycle with the same or a different duration or involving other people.

The elements will be selected for inclusion in one sprint or another depending on their priority. Higher priority must be given to the more complex and risky elements, which are the ones with greater potential for learning about the system. The suggestion is to pick first:

- Use cases that represent the most critical business processes, for example, those that help the company achieve its organizational goals, such as obtaining profit.

- High-importance (or high-exposure) risks, that is, those with high impact and a high probability of becoming problems.

- Urgent change requests, for example, those that demand architecture refactoring.

When considering the elements of highest priority, other elements with lower priorities, but closely related to the higher priority ones, may be added to the same sprint for convenience. The important thing is that the total effort assigned to the sprint does not surpass the team capacity.

## 5.8 Monitoring a project

*Chapter 5 · p. 85*

Now that we have a project divided into products with each product divided into use cases, the size of which is known we can use a system to monitor whether the project is running in schedule or not. First, take the total story points of the project and divide it by the number of linear days of the complete project. In our example, it would be a total of Table 5–27, 1760 divided by the duration of the project, which is 118 days. The total is 14.9 story points. This is the number of story points expected to be delivered each day, and it is compatible with the total size of all teams that is 16 people.

In Bridge, we usually use a monthly report to allow the team and other stakeholders to watch the pace of the project. We could be very accurate by observing how many business days there is in each month, but in this example, we simply consider that a month have 20 working days.

Then the project would take 118/20 5 5.9 months (ok, 6!) and should deliver in average 14.9 3 20 5 298 story points per month. That would allow us to draw a burn up chart to monitor this project as in Fig. 5–4.

The “Estimated” line is easy to obtain. It starts in 0 and each month we add the number of expected story points to be delivered (298 in our example) until the last position that must correspond to the total number of story points of the project.

For the “Obtained” line, data are captured from the agile teams. Each time a team finishes a use case, the number of story points of that use case is added to the delivered story points of that team in that month. At the end of the month, we simply sum the number of delivered story points by each team.

In Fig. 5–4, we can see that the team did not deliver as expected in the first and second months (this is usually the case, as the project is initiating, and all the team is learning about it). In the third and fourth months, they accelerated and not only returned to the expected productivity but surpassed it. With only 2 months lasting until the end of the project, there is a good chance that this team would meet the schedule at the end of the sixth month.

**Figure 5–4: Burn-up chart of a project that seem to be going well.** *(p. 86)*

> **Diagram content (transcribed from the figure image):** "Pace of the Project" line chart, x = sprint 0–6, y = cumulative points 0–2000: Estimated line rises linearly to ~1750 at sprint 6; Obtained line follows closely (~1300 at sprint 4, slightly ahead) — project on pace.

**Figure 5–5: Burn-up of a project that is dangerously delayed.** *(p. 86)*

> **Diagram content (transcribed from the figure image):** "Pace of the Project": Estimated linear to ~1750 at sprint 6; Obtained much lower (~620 at sprint 4) — project clearly behind schedule, re-planning needed.

In Fig. 5–5, we see a team (or set of teams that is not able to deliver the story points as planned). That project probably will not be fully delivered at its end. The teams should have taken some correction to path after perceiving that they could not reach the expected results after month 1 and 2. However, it seems that nothing was done, and that is moving the project to failure or delay.

**Figure 5–6: Burn-up chart of the SISMOB project.** *(p. 87)*

> **Diagram content (transcribed from the figure image):** Cumulative progress (0–100%) over 12 periods: estimated vs obtained curves almost overlapping, reaching 100% at period 12 (monitoring with percentage of completed effort).

In Fig. 5–6, we see the real burn-up chart for project SISMOB Phase 3 during all its 18 months of development.

## Questions (Chapter 5)

1. How do you establish a list of priorities for use cases?

2. Why estimating software development effort is so difficult? Which are the obstacles?

3. Which elements an agile software team must consider in order to attribute effort for a product?

4. Why is the rounded Fibonacci series used to assign story points instead of the natural numbers?

5. How a duration of a sprint can be decided?

This page intentionally left blank

