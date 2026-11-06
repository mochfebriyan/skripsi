<!-- Knowledge file: Chapter 16 — Interface tier design -->
> **About this file.** Chapter 16 of a cleaned, AI-ready edition of Wazlawick, R. S. (2024). Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-443-13739-6.  
> **Covers:** Interface tier design with IFML: view containers, view components (list, details, form), events, navigation and data flows, actions, interaction patterns (search, master-detail, wizard, CRUD), deriving IFML from SSDs.  
> **Use this file when:** designing UI flows/wireframes from use cases (IFML), or common screen patterns.  
> **Sections:** 16.1 Introduction to interface tier design (p. 330); 16.2 View containers (p. 330); 16.3 View components (p. 333); 16.4 Flows (p. 336); 16.5 Web interface patterns (p. 340); 16.6 Connecting the IFML model with system operations (p. 343)  
> **Contains:** 24 figures transcribed as text, 0 code listings.

# Chapter 16: Interface tier design

*Source: Wazlawick, Object-Oriented Analysis and Design for Information Systems, 2nd ed. (Elsevier, 2024), starts p. 330*

## Key topics in this chapter (Chapter 16)

- The Interaction Flow Modeling Language (IFML)

- View components

- Web page patterns

- Operations in IFML

## 16.1 Introduction to interface tier design

*Chapter 16 · p. 330*

The interface tier design of a system depends fundamentally on the detailed use cases or system sequence diagrams because the interface must allow a user to follow all use case flows. Design class diagrams and contracts may be very useful as well.

During interface design, the nonfunctional requirements that were annotated with the use cases should be revised again, because they may contain indications on how to design the use case interface.

The Interaction Flow Modeling Language (IFML) is an OMG standard^1 for modeling user interfaces compatible to UML. It was inspired in the language WebML (Ceri et al., 2003). A Web IFML editor is available in https://editor.ifmledit.org/ (Accessed 21 August 2023).

This chapter intends to present the most fundamental concepts of IFML and its modeling potential. It is important to remark that this standard does not deal with interface appearance (colors, position, and size of components), but only with the sequential flow of user operations from one interface element to the others. If you are interested in knowing and using a free design system that was built with concerns of user experience and user interface, you can try using the Bold Design System, developed by the Bridge Lab team to improve and standardize our products. The Bold design system is available at https://bold.bridge. ufsc.br/ (Accessed 30 August 2023).

## 16.2 View containers

*Chapter 16 · p. 330*

View Containers are the interface elements that are effectively accessed by the user, such as a Web page or a smartphone screen. Typically, a view container may contain other view containers as well as view components that, as is seen below, are the elements of an interface that interacts with the user.

For example, Fig. 16–1 presents a view container that contains two view containers.

> *Footnote 1:* Object Management Group. Available at https://www.omg.org/spec/IFML/1.0/PDF. (Accessed 21 August 2023). 

331

**Figure 16–1: View containers.** *(p. 332)*

> **Diagram content (transcribed from the figure image):** IFML view containers: a top-level "[D,L] View Container" (D = default, L = landmark) containing "Subview Container 1" and "Subview Container 2".

**Figure 16–2: Default and landmark view containers.** *(p. 332)*

> **Diagram content (transcribed from the figure image):** Four sibling view containers: "[D,L] View Container 1", "[L] View Container 2", "[L] View Container 3", "View Container 4" (landmark containers reachable from anywhere; default shown first).

Also, in Fig. 16–1, the main container shows special properties indicated by the label “D” and “L”:

- [D] indicates the default view container of an application. When a user enters this application, the only page marked with [D] (there can be only one) will be accessed by default.

- [L] represents a landmark page or area. This means that the page or area is directly accessible from any other page included in the same area. Thus it avoids the need to create lots of flows to pages that must be accessed from many places.

In Fig. 16–2, we see an application with four pages. View container 1 is the default page. View containers 1–3 are landmark pages, and therefore, they are directly accessed from any page in this application. View container 4 would only be accessible by a direct link from another page because it is not landmark. In practice, for each page in this application, an upper menu will be rendered with links to view containers 1–3.

Other stereotypes that can be used with containers are:

- «Window»: a view container that is rendered as a window.

- «Modal»: a view container that is rendered as a window that prevents interaction with any other element of the interface, except for the modal.

- «Modeless»: a view container that is rendered as a window that allows interaction with other windows in the screen.

## 16.3 View components

*Chapter 16 · p. 333*

View components are the most basic elements in an IFML specification. They represent the interface elements that accept input from the user and that present information to the user. View components may be directly associated to design classes in the domain model and allow viewing data about instances of these classes.

In respect to view components, IFML is extensible. Initially, a small number of options is provided, but they can be extended and refined to support many kinds of interfaces. The three options originally defined with the standard are:

- Details: Displays information about a single object.

- List: Displays information about multiple instances of a class in the form of a list.

- Form: Allows form-based data entry and presentation.

There are other view components and new ones may be defined. This chapter presents details on the most fundamental ones. For each kind of view component, an UML stereotype is presented.

### 16.3.1 Details — 16.3 View components

The details view component presents information about a single object of a given class. It is defined by the following properties:

- A name, which is chosen by the designer.

- An entity or source of data, which is usually a class from the design class diagram.

Additionally, some implementations of the standard define the property display attributes, which is a list of attributes from the class to be displayed when the details view is rendered.

Most view components such as details also allow for the definition of one or more conditional expressions that work like selectors or filters over the set of instances to be shown. Usually, those conditions are used in conjunction with parameter bindings, which are associated to the navigation flows between components and may carry one or more values to serve as arguments in order to filter the set of instances and show only the desired one.

For all IFML examples beyond this point, the domain model shown in Fig. 12–1 is used as reference.

Fig. 16–3 presents a details view component intended to show data about a proposal in SISMOB. The component is still isolated from any data flow, but there is already a data binding that says that it will be filled with instances of class Proposal.

Fig. 16–4 shows a possible Web rendering for the details view component.

The final rendered page may vary, because it is possible to add style definitions so that interfaces with different designs and appearance may be produced.

### 16.3.2 List — 16.3 View components

The view component list presents one or more attributes of a set of instances of a class in the form of a list. A list and its variations are used when a view like a menu is necessary for the user to select one or more elements and perform actions with them. The properties of lists are the same as those of the details view component.

**Figure 16–3: A details component.** *(p. 334)*

> **Diagram content (transcribed from the figure image):** IFML view container "View Proposal" with a «Details» view component "View Proposal" bound by «DataBinding» to Proposal.

**Figure 16–4: A possible rendering of Fig. 16–3.** *(p. 334)*

> **Diagram content (transcribed from the figure image):** Rendered mock-up of the «Details» component: form fields id, Name, Status, Priority, Validity, Qualified for decision.

It is possible, for example, to define list for selecting proposals, as shown in Fig. 16–5.

Observe that again the data binding is the class Proposal, meaning that data about instances of it may be shown in the lines of the list. Although not seen in the image, a list may also define which fields (attributes) will be shown, and it can have filters to select which instances will be included in the list. Fig. 16–6 shows an example of a still unpopulated list for Proposal showing the attributes name, status, and priority.

**Figure 16–5: A list view component.** *(p. 335)*

> **Diagram content (transcribed from the figure image):** IFML view container "List of Proposals" with a «List» component "List of Proposals" («DataBinding» Proposal) and an event "selected" (circle with check mark).

**Figure 16–6: A renderization of a list view component.** *(p. 335)*

> **Diagram content (transcribed from the figure image):** Rendered list mock-up: table with columns Name, Status, Priority; each row has a selection arrow (▷).

The triangles in the figure indicate that the list may be clicked, and when it happens, the default event selected (see Fig. 16–5) will be triggered.

### 16.3.3 Form — 16.3 View components

A form is used for data input. It is very useful for creating new instances and for providing parameters for searches, queries, and commands.

A form is composed of a set of fields. Each field holds an alphanumeric value. There are text fields, selection fields, and multiselecting fields, and others may be defined.

A form may or may not be associated to a class. If it is associated to a class, then its fields are associated to the attributes of that class. Otherwise, the fields are not associated to any class, as in the case of Fig. 16–7, which presents a form with two fields (unseen in the figure) for username and password.

Forms that are used to collect parameters for a query or command usually do not need to be associated to classes. Fig. 16–8 presents its rendering.

**Figure 16–7: A form view component.** *(p. 336)*

> **Diagram content (transcribed from the figure image):** IFML container "[D,L] Login" containing a «Form» component "Login data".

**Figure 16–8: A possible renderization for a form.** *(p. 336)*

> **Diagram content (transcribed from the figure image):** Rendered login form: fields Username and Password.

## 16.4 Flows

*Chapter 16 · p. 336*

A flow is an oriented connection between two view containers or view components. Flows may be used not only to define navigation possibilities between pages, but also to define data dependencies. For example, selecting an element in a list view component may cause information about the element to appear in a details view component. This can be accomplished by defining a flow from the list to the details. Fig. 16–9 shows a flow that starts at the event “selected” in the list of proposals. This event is attached to a flow that sends control to the details view component. The effect of this interaction is that the proposal selected from the list will be shown in the details area of the interface. As both view components are inside the same container, they both will be seen in the same page.

### 16.4.1 Navigation flow — 16.4 Flows

Navigation flows are a type of flow that is rendered as a clickable link in its origin page or view component. When the link is clicked, it navigates to the destination view container or view component. The navigation flow is represented by an arrow.

**Figure 16–9: A renderization of a page with a list and a details view components, and a flow between them. (A) Before selecting line “d.” (B) After selecting line “d.”** *(p. 337)*

> **Diagram content (transcribed from the figure image):** Rendered list of proposals (A) rows with Name/Status/Priority; (B) after selecting row "dddd…", a details panel below shows Name, Status, Priority, Validity, Qualified for decision of the selected proposal.

Fig. 16–10 shows an example of a navigation flow between two containers. The resulting rendering of the origin page contains a link to the other page, as shown in Fig. 16–11.

If the flow had its origin at the list view component, as in Fig. 16–12, then each line in the list would have an individual link to the details page.

### 16.4.2 Data flow — 16.4 Flows

Data flows are a kind of flow that is not rendered but that defines data dependency between view components. Dashed arrows represent data flows.

Data flows do not define navigation between view components. They are used to get values from one component without navigating to/from it. They are particularly useful when a component needs data from more than one component. The following sections present examples of data flows that get data from different sources.

**Figure 16–10: A navigational flow between two containers.** *(p. 338)*

> **Diagram content (transcribed from the figure image):** IFML navigation: "[D,L] Wellcome page" container with an event "select" whose navigation flow (arrow) leads to the "Main menu" container.

**Figure 16–11: A renderization of the pages connected by a navigational flow. (A) before clicking in “Main Menu,” a link defined by the user inside the container. (B) after clicking in “Main Menu”; the link returning to Welcome page appears because this page is landmark [L].** *(p. 338)*

> **Diagram content (transcribed from the figure image):** Rendered screens: (A) Welcome page with a link "Main Menu"; (B) Main Menu with a link "Wellcome page" (landmark navigation).

**Figure 16–12: A data binding between two views.** *(p. 338)*

> **Diagram content (transcribed from the figure image):** IFML within one View Container: «List» "List of Proposals" («DataBinding» Proposal) with event "selected" → navigation flow carrying parameter binding id -> prop_id → «Details» "A proposal" («DataBinding» Proposal) with condition id = prop_id.

### 16.4.3 Parameter binding — 16.4 Flows

A parameter binding is a piece of information that is transmitted from the origin to the destination of a flow. A parameter binding has a name and a value. The name and value are sent by the origin element, and they are matched to one of the attributes (usually a key) of the class in the destination element.

A flow may have a multiple parameter binding, passing a set of values instead of one. Usually, object keys or attribute values are passed by parameter bindings. By default, a flow from a view component binds the key of the selected object at the origin component and takes it to the destination, where it can be used, for example, by a conditional expression.

With flows and parameter binding, it is possible to use a view component to define which elements are shown in another view component.

The IFML diagram shown in Fig. 16–12 shows a list of proposals with a flow to a details view component. The details view has a key attribute id. As the id key of the selected book at the list is bound to the flow by prop_id that goes to the details view, only a proposal in which id is identical to prop_id is shown when the details view is rendered.

When the user selects a proposal in the list, by clicking the respective link, the details view presents information about the proposal.

Parameter binding may also be used to associate a form to another view component. For example, the form may provide a search field, and a list would present only the elements that satisfy some search criteria.

Fig. 16–13 shows an example where a search field is used to find the proposal of a given municipal manager. The user may type the proposal’s name or part of it in the search field, and the results are shown in the Proposals list.

**Figure 16–13: A view that takes keys from two different views.** *(p. 339)*

> **Diagram content (transcribed from the figure image):** IFML search pattern: container "Search screen" with «Form» "Search" (event "search", parameter binding s_string -> name_part) and «Details» view component («DataBinding» MunicipalManager, data flow mun-id -> municipal); both flow into container "Results" with «List» view component («DataBinding» Proposal) filtered by "name includes name_part" and "municipal = municipal manager.id".

Initially, the focus is on the form in Search Screen. When the event search is triggered, the flow goes to the list view in Results. This list view has two binding conditions: the text entered in the form must be included in the name of the proposal, and the id of the municipal manager taken from the details in Search Screen must coincide with the id of the municipal manager linked to the Proposal.

## 16.5 Web interface patterns

*Chapter 16 · p. 340*

Most web interface patterns presented in this section are adapted from Ceri et al. (2003) and Tidwell (2005).

### 16.5.1 Cascade index — 16.5 Web interface patterns

A cascade index is a sequence of menus based on lists that eventually reaches a details view. For example, a user could begin by selecting a Proposal. Then, the user could select a list of Sending from a selected proposal, then access a list of proposal’s assessments, and finally one assessment individually. Fig. 16–14 illustrates that pattern.

In the diagram of Fig. 16–14, as the parameter bindings are default, the flows carry the id’s of the selected elements. Those id’s may be used by the conditional expressions at the destination view component to define which element(s) is(are) to be shown. As the id is the default data carried by a parameter binding, it is not usually shown in the diagram.

One variant of this pattern consists of showing some data from the object selected in one of the intermediary lists. Fig. 16–15 illustrates that situation.

There, when a proposal is selected, the interface shows the proposal’s details and a list of sendings for further selection.

### 16.5.2 Filtered index — 16.5 Web interface patterns

In some cases, it may be necessary to show a list with selected elements. For example, the SISMOB has in average 20–40 thousand proposals being analyzed and executed at the same time; in this case it would not be feasible for a user to simply browse for a proposal in that list. A filtered list could be used instead, for example, asking the user to provide a keyword to show a reduced list of proposals.

**Figure 16–14: A cascade index.** *(p. 340)*

> **Diagram content (transcribed from the figure image):** Multi-level master-detail across four containers: "List of Proposals" («List» Proposals) —selected→ "List of Sendings" («List» Sendings) —selected→ "List of Assessments" («List» Assessments) —selected→ "Assessment" («Details» Assessment).

**Figure 16–15: A variant of the cascade index that shows details of the intermediary objects.** *(p. 341)*

> **Diagram content (transcribed from the figure image):** Same navigation with details shown at each step: "List of Proposals" («List» Proposals) —selected→ "List of Sendings" containing «Details» Proposal and (data flow) «List» Sendings; Sendings —selected→ "List of Assessments" containing «Details» Sending and «List» Assessments; Assessments —selected→ "Assessment" («Details» Assessment).

**Figure 16–16: A filtered index.** *(p. 341)*

> **Diagram content (transcribed from the figure image):** Search–results–details: "Search Page" («Form» Search Proposal, event submit) → "Results" («List» Proposals) —selected→ "Details" («Details» Proposal).

This pattern is accomplished by a connection between a form, a list, and a details component, as shown in Fig. 16–16.

A maximum number of results may be defined for this list so that unnecessarily large lists are not presented.

### 16.5.3 Guided tour — 16.5 Web interface patterns

A guided tour is a pattern that allows one to visualize details of a set of objects one at a time by using scroll operations. It is implemented by using two or more events that will be rendered as buttons, as seen in Fig. 16–17.

**Figure 16–17: A guided tour.** *(p. 342)*

> **Diagram content (transcribed from the figure image):** Guided tour: container "Guided Tour" with «Details» Proposals («DataBinding» Proposal) and two events "backward" and "forward" that navigate to the previous/next proposal.

**Figure 16–18: Viewpoints.** *(p. 342)*

> **Diagram content (transcribed from the figure image):** Expand/shrink: "[D] Summary" container with «Details» Proposal summary (event expand) → "Complete Information" with «Details» Complete proposal (event shrink back to the summary).

### 16.5.4 Viewpoints — 16.5 Web interface patterns

Sometimes, it may be interesting to present different faces of certain objects in different moments. For example, summarized data about a proposal may be presented by default, but that data may be expanded or contracted again at the user’s will.

In order to implement the viewpoints pattern, two or more details components may be defined for the same class, with different sets of attributes. Flows may be defined between the different components to allow the user to change from one view to another, as shown in Fig. 16–18.

**Figure 16–19: Overview plus detail.** *(p. 343)*

> **Diagram content (transcribed from the figure image):** Overview/details in one container "Proposals Overview/Details": «List» Proposals Overview —selected→ «Details» Proposal Details (both bound to Proposal).

### 16.5.5 Overview plus detail — 16.5 Web interface patterns

The overview plus detail pattern is very common in applications such as email browsers, but it can be applied to a variety of other situations. The idea is to have in the same page a scrolling list of elements and the details view of one selected element in a region next to the list.

Fig. 16–19 shows an IFML definition that uses this pattern with a list and a details view component linked to it by a flow. They are rendered in the same window.

### 16.5.6 Top-level navigation — 16.5 Web interface patterns

Top-level navigation is a frequent pattern in Web pages where a top-level menu allows access to different areas of the site. The example in Fig. 16–20 illustrates top-level navigation being defined by a set of landmark areas, each containing one or more pages, which would be rendered as submenu selected options.

## 16.6 Connecting the IFML model with system operations

*Chapter 16 · p. 343*

IFML allows operations to be modeled by using actions (Fig. 16–21) that are executed after some interface events (menu selection, button pressed, etc.) happen. These components perform all the operational logic of the system that is fruit of the detailed use cases and/or system sequence diagrams.

The operation components do not hold or render information; they just process information. Therefore they are represented graphically outside the containers.

**Figure 16–20: Top-level navigation being defined by a set of landmark areas.** *(p. 344)*

> **Diagram content (transcribed from the figure image):** Landmark top-level menu: "[D,L] Login" (subcontainers Sign in, Forgot my password, Create new account); "[L] My Proposals" (View my proposals); "[L] My Assessments" (View assessments due, View concluded); "[L] Budget" (Reports, Actions).

**Figure 16–21: An action component calling a system operation.** *(p. 344)*

> **Diagram content (transcribed from the figure image):** IFML action symbol: hexagon-like box labelled get_assessment (an action triggered by an event, calling a system operation).

Every operation component should have at least one input flow. Sometimes all the information the operation needs is obtained from a single view component, but sometimes more than one view component may be necessary to supply all the data needed by an operation. In this case, the operation must receive one navigation flow and a set of data flows.

Operation components have special output flows:

- OK flow, which defines where the focus goes when the operation is successfully performed for every object.

- Fail flow, which defines where the focus goes when the operation fails for at least one of the objects affected by it.

### 16.6.1 IFML models for CRUDL operations — 16.6 Connecting the IFML model with system operations

This section shows how to implement a CRUDL-style interface for managing information about publishers using IFML view components and system operations.

**Figure 16–22: A simplified model for the CRUDL pattern.** *(p. 345)*

> **Diagram content (transcribed from the figure image):** CRUD with actions and error handling: "[D] Manage Proposals" contains «List» List of Proposals with events create new proposal, selected, update, delete. create new proposal → container "Create new proposal" («Form» Proposal, event save) → action "Create proposal": ok → back to list; fail → "Error message create" (event → back to the form). selected → "View Container" («Details» View Details, event return → list). update → "Update Proposal" («Form» Proposal, save) → action "Update proposal": ok → list; fail → "Error message update" (return → form). delete → action "Delete Proposal": ok → list; fail → "Error message delete" (return → list).

The CRUDL main page, Manage Proposals, presents a list of existing proposals (associated to that specific municipal manager). The creation of a new proposal is initiated by clicking on a button on the main page that gives access to a form container where the data about the proposal will be filled. If the creation of a new proposal is successful, control returns to the main list, and the new proposal will appear in that list. If there is an error, control goes to an error page, from which it is possible to return to the main page (Fig. 16–22).

The second operation of a CRUD, retrieve, is represented by the flow that navigates from the list to the details page.

The third operation, update, allows a publisher to be selected in the main list, and the attributes of the selected proposal are used to fill the fields of a container form with Proposal as the source class. There the nonimmutable ones can be edited by the user and saved, with the flow returning to the main list.

Finally, the operation for deleting a proposal is added. A delete operation may be accessed from the main list. If it succeeds, the flow returns to the main list. Otherwise, an error message is shown.

### 16.6.2 Use case interface modeling with IFML — 16.6 Connecting the IFML model with system operations

Working with interfaces is possible at this time because use cases have already been explored and the team has a deeper understanding about the interface structure and the user needs, which allow them to design an acceptable interface.

In this section, we will revisit the sequence diagram of Figure 7–8, now reproduced as Fig. 16–23 and using it as an example on how to design the user interaction with the interface: Fig. 16–24 shows a possible IFML diagram to model the interaction of the user with the interface of this system.

**Figure 16–23: Sequence diagram used as example.** *(p. 346)*

> **Diagram content (transcribed from the figure image):** The SSD of Fig 7–8 (assess project with alt [dto_project* is empty] → MSG.049 and ref SQ.39 insert assessment; main flow list_projects, get_assessment, set_assessment, success, MSG.342) used as the basis for the IFML model of Fig 16–24.

**Figure 16–24: IFML diagram for updating assessment. IFML, Interaction Flow Modeling Language.** *(p. 346)*

> **Diagram content (transcribed from the figure image):** IFML model derived from that SSD: "[D] Search Proposal" container with «Form» Search Form (event search) → «List» Search Results («DataBinding» Proposal, event selected) and «Details» Reviewer («DataBinding» Person); selected → action list_projects: [empty] → container MSG49 (→ action SQ39) ; [ok] → container "Proposal" with «Form» Proposal and «Form» Assessment filled via action get assessment; Assessment event update → action update_assessment → event → container MSG342 → ok → back to Search Proposal.

In order to prepare an interface design based on that sequence diagram, the team should look at the system operations, including their parameters and results:

- Any system operation, be it a command or query, must be activated somewhere in the interface. The activation event can be obtained by clicking a button or a link, by selecting an item from a list, etc. Sometimes the same event may activate more than one system operation: if two or more system operations happen just after a system event (left side of the sequence diagram), then they are possibly activated by the same user action.

- Any parameter a system operation has must be obtained somewhere. Some parameters could be obtained from external sources (such as a clock), but most parameters would be obtained in the interface. Thus for most parameters there will be an interface view component that allows the user to introduce the necessary data.

- Any result obtained by a system query must be presented somewhere. Some results may be hidden from the user in some cases, but usually they are presented. View components such as lists, details, and others may be used to show system query results.

## Questions (Chapter 16)

1. Why IFML notation needs dataflows that are not navigable?

2. Construct an IFML model that uses filtered index and viewpoints simultaneously.

3. Look at Fig. 16–16 and make explicit the parameter bindings necessary for this model.

This page intentionally left blank

