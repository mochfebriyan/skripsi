# OOAD for Information Systems (Wazlawick, 2024) — Knowledge Pack Index (start here)

Cleaned, structured, AI-ready edition of *Wazlawick, R. S. (2024). Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-443-13739-6*. Converted from the PDF and verified against it.

## The method in one line

General view & business use cases (Ch2) → business process/state modeling, BPMN (Ch3) → system use cases & requirements (Ch4) → planning (Ch5) → expanded use cases (Ch6) → system sequence diagrams / system operations (Ch7) → conceptual model (Ch8–11) → OCL contracts (Ch12) → domain design (Ch13) → code (Ch14) → tests (Ch15) → interface design, IFML (Ch16) → persistence (Ch17).

The running example throughout is **SISMOB** (a Brazilian Ministry of Health system to monitor construction works funded for municipalities: proposals, assessments, funds allocation, phases).

## Files in this pack

- **`01_Ch01_Introduction_OO_and_Agile.md`** — Ch. 1 Introduction. Introduction: the book's approach, object-oriented systems development, agile (Scrum) development.
- **`02_Ch02_General_View_Business_Use_Cases_Backlog.md`** — Ch. 2 General view of the system. General view of the system: early effort estimation, acceptance criteria, project/goal/product structure, product backlog, business use cases, business actors and workers, automation opportunities (SISMOB example).
- **`03_Ch03_Business_Modeling_BPMN_State_Machines.md`** — Ch. 3 Business modeling. Business modeling: BPMN tasks, events, gateways, pools and lanes, recommendations; state machine diagrams for state-dependent aspects of a business.
- **`04_Ch04_High_Level_Requirements_System_Use_Cases.md`** — Ch. 4 High-level requirements. High-level requirements: system actors, system use cases and criteria for a good use case (single session, interactive, consistent result, essential, brief, system boundary), deriving use cases from business use cases, BPMN and state diagrams; requirement types (evident/hidden functional, non-functional, supplementary, ISO/IEC 25010), preliminary conceptual model, CRUDL pattern.
- **`05_Ch05_Use_Case_Based_Project_Planning.md`** — Ch. 5 Use case-based project planning. Effort estimation (ad hoc, parametric, use case/story points, technical and environmental factors), linear time, sprint duration, use case priority, project monitoring.
- **`06_Ch06_Expanded_Use_Cases.md`** — Ch. 6 Expanded use cases. Expanded use cases: main flow, alternate flows (exceptions, variants), writing recommendations, included use cases and fragments, other sections, expansion of stereotyped (CRUD/report) use cases.
- **`07_Ch07_System_Operations_System_Sequence_Diagrams.md`** — Ch. 7 System operations. System sequence diagrams with actor, interface and controller; system events vs system commands and queries; stateful vs stateless; alternate flows in SSDs.
- **`08_Ch08_Conceptual_Modeling_Fundamentals.md`** — Ch. 8 Conceptual modeling: fundamentals. Conceptual model fundamentals: attributes (types, initial values, derived, enumerations, primitive types, «unique»), concepts, associations (roles, multiplicity, derived, aggregation/composition, n-ary).
- **`09_Ch09_Conceptual_Modeling_Data_Structures.md`** — Ch. 9 Conceptual modeling: data structures and organization. Collections (set, bag, sequence, ordered set, map, partition, relation), organization of the conceptual model (generalization, association classes, roles vs subclasses), modal classes (states), invariants.
- **`10_Ch10_From_Use_Cases_to_Conceptual_Model.md`** — Ch. 10 From use cases to conceptual model. Iterative construction of the conceptual model from expanded use cases: finding concepts, attributes and associations; dependent vs independent concepts; worked SISMOB example.
- **`11_Ch11_Conceptual_Model_Patterns.md`** — Ch. 11 Conceptual modeling: patterns. Analysis patterns: high cohesion, specification classes, quantity, measure, strategy, composite, organizational hierarchy, object joining, account/transaction, range/interval, temporal patterns (history, temporal, bitemporal).
- **`12_Ch12_Functional_Modeling_OCL_Contracts.md`** — Ch. 12 Functional modeling with object constraint language contracts. Functional modeling with OCL contracts: preconditions, exceptions, postconditions for system commands and queries, return values, examples.
- **`13_Ch13_Domain_Tier_Design.md`** — Ch. 13 Domain tier design. Domain tier design: visibility (association, parameter, local, global), dynamic models from contracts, delegation vs concentration, design class diagram.
- **`14_Ch14_Code_Generation_Python.md`** — Ch. 14 Code generation. Code generation in Python: classes, attributes, basic get/set/add/remove methods by association type, collections, qualified associations, association classes, methods from dynamic models.
- **`15_Ch15_Testing.md`** — Ch. 15 Testing. Testing: functional tests derived from use cases and contracts, unit tests, stubs and drivers, test-driven development, acceptance tests.
- **`16_Ch16_Interface_Tier_Design_IFML.md`** — Ch. 16 Interface tier design. Interface tier design with IFML: view containers, view components (list, details, form), events, navigation and data flows, actions, interaction patterns (search, master-detail, wizard, CRUD), deriving IFML from SSDs.
- **`17_Ch17_Data_Persistence.md`** — Ch. 17 Data persistence. Data persistence: mapping classes, attributes and associations (1, 0..1, *, ordered, bag, qualified, association classes, n-ary, inheritance) to relational tables; virtual proxies, caches, transactions.
- **`18_Bibliography.md`** — reference list.

## Where to look for common analysis & design tasks

| Task | Chapter / file |
|---|---|
| Model AS-IS / TO-BE business process (BPMN, swimlanes) | Ch3 `03_…` |
| Status/life cycle of a business object (state machine) | Ch3.3 `03_…`, Ch9.3 `09_…` |
| Business use case diagram, actors vs workers, what to automate | Ch2.6 `02_…` |
| Derive system use cases / functional requirements from BPMN or state diagrams | Ch4.4–4.6 `04_…` |
| Functional vs non-functional / supplementary requirements (ISO/IEC 25010) | Ch4.7 `04_…` |
| Find missing use cases (CRUDL) | Ch4.8.2 `04_…` |
| Use case specification: main & alternate flows | Ch6 `06_…` |
| System sequence diagram | Ch7 `07_…` |
| Class diagram / conceptual model (and from use cases) | Ch8–10 `08_…`–`10_…` |
| Analysis patterns (history, measures, discounts, hierarchies…) | Ch11 `11_…` |
| Pre/postconditions of operations (OCL) | Ch12 `12_…` |
| UI flow / wireframe structure (IFML) | Ch16 `16_…` |
| Class diagram → database tables | Ch17 `17_…` |
| Effort estimation with use case points | Ch5 `05_…` |

## Conversion notes

- All 251 figures (BPMN, use case, class, state, sequence, IFML diagrams, charts) were transcribed from the figure images into structured text ("Diagram content") placed under each figure caption. The original markdown only had unreadable OCR fragments for these.
- Code listings (OCL contracts, Python, pseudo-code) were re-extracted from the PDF with original line breaks and indentation, in fenced code blocks (```ocl / ```python). 7 listings missing from the original markdown were restored.
- 1,113 broken en-dash characters (shown as "�") fixed — figure/table references like "Fig. 2–3" and ranges like "6–12 h" are readable again; UML stereotypes restored as «business», «worker», «imm», «unique», etc.
- Removed page headers/footers, DOI/copyright footers, table of contents and back-of-book index; printed page numbers kept at each section heading (`p. N`) and figure for citation; sentences split by page breaks or figures re-joined.
- Headings normalized: Chapter (#) → section N.M (##) → subsection N.M.K (###, carries its parent section name so each retrieved chunk is self-describing).
- Footnotes kept as "Footnote N" quotes next to where they appeared.
