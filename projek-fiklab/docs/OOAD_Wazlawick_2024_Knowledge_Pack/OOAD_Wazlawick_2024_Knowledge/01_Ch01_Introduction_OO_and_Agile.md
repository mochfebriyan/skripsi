<!-- Knowledge file: Chapter 1 — Introduction -->
> **About this file.** Chapter 1 of a cleaned, AI-ready edition of Wazlawick, R. S. (2024). Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-443-13739-6.  
> **Covers:** Introduction: the book's approach, object-oriented systems development, agile (Scrum) development.  
> **Use this file when:** the question is about the overall method of the book, OO development, or how agile/Scrum fits.  
> **Sections:** 1.1 This book (p. 1); 1.2 Object-oriented systems development (p. 2); 1.3 Agile software development (p. 2); 1.4 Discussion (p. 4)  
> **Contains:** 2 figures transcribed as text, 0 code listings.

# Chapter 1: Introduction

*Source: Wazlawick, Object-Oriented Analysis and Design for Information Systems, 2nd ed. (Elsevier, 2024), starts p. 1*

## Key topics in this chapter (Chapter 1)

- Object-Oriented Systems Development

- Agile Software Development

## 1.1 This book

*Chapter 1 · p. 1*

There is a vast literature that aims at presenting UML (Unified Modeling Language)^1 and other diagrams by using a syntactical approach, such as Miles and Hamilton (2006). There are also a significant number of books about development processes and management activities, such as Satzinger et al. (2011). However, there are relatively few books that go deep into the presentation of best practices that allow the effective application of object-oriented techniques in software development in the real world, especially if we consider the new generation of agile methods. This means that despite the vast literature in this area, many questions faced by developers are still left unanswered.

In our approach, agile principles and rules adopted by Scrum^2 are largely accepted. As Scrum does not explicitly explain how to develop software, but how to manage the software development process, this book shows how to use object-oriented techniques to improve the team’s ability to understand and communicate aspects of the problem and solution.

Furthermore, this book presents some original concepts and other details on topics as follows:

- Objective criteria to identify use cases and decide when to subdivide them or not.

- A technique to systematically derive system use cases from BPMN (Business Process Modeling and Notation) and machine-state diagrams.

- A technique to expand use cases that reduces the disparity among descriptions created by different analysts.

- System sequence diagrams built with actor, interface, and control (instead of actor and system only) to help realize a clear difference between system events and system operations.

- An original approach for writing system commands and queries contracts with the use of the Object Constraint Language (OCL) (Object Management Group, 2010) that allows for automatic generation of running code and not only postcondition checking.

> *Footnote 1:* http://www.uml.org/

> *Footnote 2:* https://www.scrum.org/resources/scrum-guide

1

- An adaptation of Fowler’s (2003) analysis patterns to UML and restructuring and evolving some of those patterns to simplify their identification and application in practice.

- A systematic technique to generate dynamic object models from OCL contracts, which follows good design patterns and significantly reduces the amount of code necessary for running an application, avoiding, for example, redundant verifications.

- An interface tier design presented with the use of IFML (Interaction Flow Modeling Language).

The aforementioned features are useful for producing high-quality software that is well organized, based on a multitiered architecture, and able to change or accommodate new requirements.

## 1.2 Object-oriented systems development

*Chapter 1 · p. 2*

What is object-oriented systems development? By observing the way object-oriented analysis and design are taught and practiced in some places, it can be concluded that many professionals simply adopt an object-oriented programming language or use fragments of an object-oriented-based development process without exploring the approach in full. Thus very often, they are not as effective as could be expected.

It is not sufficient to organize the system architecture in tiers and modules if the code implemented inside of it is disorganized. Some programmers organize the system adequately in classes and packages, but they still write spaghetti code inside the methods of these classes and packages. In addition, other developers still use top-down functional decomposition inside methods, which is not appropriate when using object-oriented programming. Top-down decomposition is adequate if structured programming is used instead.

In order to build code that is really object-oriented, developers should learn the techniques of delegation and responsibility assignment, which can lead to reusable code and low coupling. Those techniques are explained in this book.

It is useless to invest heavily in object-oriented CASE (computer-aided software engineering) tools without learning the way to think in terms of object-oriented modeling. The use of diagrams will not necessarily improve the quality of the software, although it may help.

## 1.3 Agile software development

*Chapter 1 · p. 2*

In relation to the development process, it can be observed that throughout the 20th century several models were proposed. These processes usually mention different stages of development, such as the so-called Waterfall Model of the 1970s (Royce, 1970). In the Waterfall Model, each stage is dedicated to one discipline, such as system requirements, software requirements, analysis, program design, coding, testing, and operation. At the end of each stage, several documents needed to be finalized, including some diagrams. In his original paper, Royce also described why this simplified staged model would not work in practice, and he proposed some other features to improve the process, as shown in the left part of

**Figure 1–1: Final version of Royce’s Waterfall Model. By Winston W. Royce - IEEE WESCON, Public Domain, https://commons.wikimedia.org/w/index.php?curid 5 88212953.** *(p. 3)*

> **Diagram content (transcribed from the figure image):** Waterfall-style document-driven process diagram (after Royce/DoD-2167): sequential stages System Requirements → Software Requirements → Preliminary Program Design → Analysis → Program Design → Coding → Testing → Usage/Operations, with review milestones (PSR Preliminary Software Review, CSR Critical Software Review, FSAR Final Software Acceptance Review) and produced documents No. 1 Software Requirements, No. 2 Preliminary Design Specifications, No. 3 Interface Design Specifications, No. 4 Final Design Specifications, No. 5 Test Plan Specifications, No. 6 Operating Instructions; many feedback arrows show iterations; on the right a simplified chain System Requirements → Software Requirements → Analysis → Program Design → Coding → Testing → Operations with a loop back to Program Design.

Fig. 1–1. Unfortunately, it seems that many people liked the simpler waterfall version seen in the right part of Fig. 1–1 and adopted it without reading the rest of the paper.

The Unified Process, which arose in the 1990s, disassociated the concept of “stage” from the concept of “discipline” (correlated activities). It placed stages and disciplines in two orthogonal dimensions, indicating that all disciplines can be exercised during all stages of the project, but with different intensities: requirements more intensely at the beginning and more tests at the end, for example (Fig. 1–2).

Still, despite its agile versions, the Unified Process remained basically an artifact-oriented model, requiring, in many cases, the construction of diagrams and other documents.

The agile revolution, from the beginning of the 21st century changed the focus of software development models, which went from processes and artifacts to people and communication.

The difference between those methods can be clarified by a metaphor. In this metaphor, the prescriptive process-based bakery of the 20th century would have at the disposal of bakers the best recipes of breads and other delicacies, and that the rule is that bakers should follow the recipes. If something didn’t work well, the recipe is corrected or complemented so that the same problem would not happen again. But with this process, the recipes become increasingly complex and difficult to follow. Also, the bakers often could spend more time discussing the recipe than effectively making bread.

With the agile bakery, something different would happen. At first, the bakery would hire experienced bakers capable of working as a team, give them an ideal working environment with the best tools and ingredients. They know how to make bread. They can develop their own recipes, based on their experiences and knowledge about the taste of the customers, which they consult frequently. Frequently they would be exchanging information about what was going on, about the best and worst recipes and thus would jointly evolve a development model based on their skills and intense communication among them and clients. That way, they would spend more time actually making breads and still experimenting with new and original recipes, quickly solving among them any problems that arise and improving their experience even more.

**Figure 1–2: A simplified view of the Unified Process. By Jakob Farian Krarup - Own work, CC0, https://commons. wikimedia.org/w/index.php?curid 5 93364952.** *(p. 4)*

> **Diagram content (transcribed from the figure image):** "Iterative Development" chart (RUP hump chart): phases Inception (I1), Elaboration (E1, E2), Construction (C1–C4), Transition (T1, T2) on a time axis; disciplines Business Modeling, Requirements, Analysis & Design, Implementation, Test, Deployment shown as effort curves — business modeling and requirements peak early, analysis & design peaks in elaboration, implementation peaks in construction, test peaks recur each iteration, deployment peaks in transition. Caption idea: business value is delivered incrementally in time-boxed cross-discipline iterations.

Bringing this metaphor to the software industry, we see that it is increasingly less important to think in terms of stages and procedures and increasing focus on the human beings who produce software and who use that same software (the user) and the quality of their communications.

As the agile manifesto says^3 , there may be documentation, contracts, processes, tools, plans, and customer negotiation, but more important is to have motivated individuals, easy interactions, collaboration, working software, and the ability to accommodate change.

## 1.4 Discussion

*Chapter 1 · p. 4*

Agile models have not changed, however, the way software is programmed. The objectoriented paradigm is still dominant today in the software industry. Most agile models also deal more with management aspects than software modeling and programming. Thus the

3 https://agilemanifesto.org/ software produced in an agile way does not rule out the construction of good models. Maybe XP—eXtreme Programming (Beck and Andres, 2004) one day has given the impression that agile development should consist of “go and program fast” without any planning. But that’s a myth. Before we start developing lines of code, we need to understand the user’s needs and pains, their context, their journey, and their obstacles. Some diagrams can help a lot in this. After understanding the problem and prioritizing features, we need to draw one or more solutions to the prioritized features. Again, diagrams can help in crafting, refining, and communicating these ideas.

Thus this book will go through several activities of software development assuming they are conducted by an agile model such as Scrum, and presenting several notations, diagrams, and languages that can be used as tools of thought so that agile teams can represent and evolve their ideas.

## Questions (Chapter 1)

1. What differentiates a process-based software development from an agile one?

2. What is UML?

3. What is Scrum?

4. Do agile methods hinder object-oriented programming? Why?

5. What is the agile manifesto and how should it be interpreted?

This page intentionally left blank

