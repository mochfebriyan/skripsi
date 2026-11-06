<!-- Knowledge file: Chapter 17 — Data persistence -->
> **About this file.** Chapter 17 of a cleaned, AI-ready edition of Wazlawick, R. S. (2024). Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-443-13739-6.  
> **Covers:** Data persistence: mapping classes, attributes and associations (1, 0..1, *, ordered, bag, qualified, association classes, n-ary, inheritance) to relational tables; virtual proxies, caches, transactions.  
> **Use this file when:** mapping a class diagram to a relational database schema (tables, keys) or persistence design.  
> **Sections:** 17.1 Introduction to data persistence (p. 347); 17.2 Object-relational mapping (p. 350); 17.3 Saving and loading objects (p. 366)  
> **Contains:** 14 figures transcribed as text, 0 code listings.

# Chapter 17: Data persistence

*Source: Wazlawick, Object-Oriented Analysis and Design for Information Systems, 2nd ed. (Elsevier, 2024), starts p. 347*

Key topics in this chapter

- Object-relational Mapping (ORM)

- Virtual Proxy

- Brokers

- Virtual Caches

## 17.1 Introduction to data persistence

*Chapter 17 · p. 347*

The availability of persistence mechanisms for commercial languages^1 has made database design much easier for many projects. With adequate tools, it is possible to automatically generate the persistence tier for a great number of information systems. For some critical and legacy systems, however, database adjustments may be still necessary to accommodate special features or to satisfy performance or security requirements.

Usually, object-oriented systems are implemented in object-oriented languages, but persistent^2 data storage is accomplished with relational databases. Although other techniques such as object-oriented databases (Won, 1990) and XML databases (Bourret, 2010) are also options for implementing permanent storage of data, the pattern ORM, object-relational mapping, is still the preferred approach.

The goal of this chapter is to explain what happens inside the persistence tier of a system when a persistence mechanism based on ORM is used. First, a good persistence mechanism requires domain and data storage to be separated into different tiers within the application. Remember that the interface tier may be modeled with use cases and IFML, and the domain tier may be designed using class diagrams and contracts as its basis. None of the aforementioned tiers addresses data storage or persistence. Persistence should be designed as a separate concern: a background system that will keep data securely and permanently in its place without interfering on the domain or interface logic.

The persistence mechanism should assure that the objects are saved in a permanent memory device, and that they are loaded from there when necessary. Domain and interface logic should not be polluted by persistence concerns.

Object-oriented design provides lots of good concepts such as encapsulation, responsibility, and delegation that help designers deal with the complexities of the logic for accessing

> *Footnote 1:* See, for example: http://www.hibernate.org/. (Accessed 31 August 2023).

> *Footnote 2:* Persistent in this context is the opposite of transient, that is, persistent information is information that must be kept until some user explicitly deletes it. Transient information is kept only during a session of use of the system. 

349 and transforming information. But when data must be stored in a more permanent way— disks and tapes, for example—the relational database is a good option because it is very efficient in terms of time usage and there are lots of optimization techniques to improve relational database operations. Thus if the team wants to work in the best of two worlds (object and relational), the mapping between them must be understood.

The literature refers to the problem of object-relational impedance mismatch (Ireland et al., 2009), because most of the good features obtained by object-oriented design are lost when a flat relational database is used.

The implementation of a persistence mechanism minimizes that problem by using a set of predefined classes not belonging to the domain tier that take care of all logic involving domain objects being saved and retrieved from a relational database.

## 17.2 Object-relational mapping

*Chapter 17 · p. 350*

A complete and detailed design class diagram (DCD) allows for the automatic generation of a relational database structure that reflects in secondary memory^3 the information that the objects represent in main memory. The following sections present some equivalence rules that should be observed when using ORM and if the team wants to minimize the objectrelational impedance mismatch.

### 17.2.1 Classes and attributes — 17.2 Object-relational mapping

The first set of rules addresses classes and their attributes. Each persistent class of the DCD corresponds to a relational table. Each attribute is a column of the table, and each instance is a line or record of the table.

The stereotypes of some attributes such as «unique», «opt», and «imm» affect the properties of the columns of the relational tables. Some of the features described here may not be implemented by some commercial database management systems. In that case, adjustments might be necessary to provide a safe implementation free from the objectrelational impedance mismatch.

Attributes stereotyped with «unique» are represented as columns marked as unique, which cannot repeat values. However, even objects with no unique attribute have an identity that distinguishes them from other objects. Even objects with the same value for every single attribute may be differentiated by their identity. In the case of relational tables, this is accomplished by defining a primary key to each relational table. A primary key, just like a unique column, should not repeat elements. An element in a primary key column should also not be null. Primary keys usually are simply sequential numbers generated automatically by the application in such a way that the same number is never generated twice for the same table. Primary keys do not correspond to any of the attributes of an object: they correspond to the object identity.

> *Footnote 3:* Secondary memory is usually slower than main memory. However, it is also much cheaper, and thus, it is widely used to store large quantities of data that do not fit in the more expensive main memory. Usually, secondary memory consists of media such as magnetic or optical disks, tapes, or solid-state drivers. Data stored in secondary memory usually cannot be processed directly by the computer unless it is loaded into main memory. Main memory is also known as RAM (random access memory), and physically, it is usually implemented by nonpersistent electronic integrated circuits.

Fig. 17–1 shows the class that is the basis for the following examples, and Table 17–1 shows the equivalent relational table with three instances of that class represented.

Although other formats could be used to specify the constraints on the columns, here they are presented as acronyms for quick reference:

- unique, means that the column cannot repeat values.

- imm, or immutable, means that the value in the column cannot be updated.

- nn, or not null, means that the column does not admit the null value. It is exactly the opposite of the «opt» or «optional» stereotype used for design classes. It is used here because not null is a more common constraint implemented in databases than optional.

- pk, or primary key, means that the column is the primary key of the table. Primary key columns in the examples of this chapter are painted in gray. If one or more columns compose the pk, all columns are necessarily immutable and not null. If only a single column is pk, then it must be unique as well. However, if the PK is composite, spreading over more than one column, then each individual column may or may not be unique, but the combination of all columns is unique.

The first column in Table 17–1 is pk_book. Notice that it does not correspond to any attribute of the reference class. Its value is artificially generated by a number sequence generator so

**Figure 17–1: A class used in examples.** *(p. 351)*

> **Diagram content (transcribed from the figure image):** Class Book to persist: {«imm» «unique» +isbn: ISBN; «imm» +title: String; «imm» +authors_name: String; +price: Money; «imm» +page_count: Natural; +/publisher_name: String; «opt» +cover_image: Image; +quantity_in_stock: Natural = 0}.

**Table 17–1: Relational table equivalent to the class in Fig. 17–1.**

Table: Book that it is unique for the whole application or at least for that table. Some authors refer to it as a surrogate key, that is, a value that has no semantic meaning and is unique systemwide, never reused, system generated, and not handled by users or application.

|pk,unique, imm,nn pk_book|unique, imm,nn isbn|imm,nn title|imm,nn authors_name|nn price|imm,nn page_count cover_image|nn quantity_in_stock|
|---|---|---|---|---|---|---|
|10001|0553286587|Rama II|Arthur C. Clarke and Gentry Lee|6.99|466|2|
|10002|0553293370|Foundation and Empire|Isaac Asimov|5.99|282|3|
|10003|0671742515|The Long Dark Tea- Time of the Soul|Douglas N. Adams|6.99|307|21|

The other columns correspond to the nonderived attributes of the reference class:

- isbn is a unique, immutable, and not null attribute. Therefore the equivalent column is unique, imm, and nn.

- title, authors_name, and page_count are nonderived attributes that are immutable and not null. Therefore the equivalent column for each one is imm and nn, but not unique.

- price and quantity_in_stock are nonderived attributes that may change but cannot be null. Therefore the equivalent column for each is nn only.

- cover_image is an optional attribute that may be updated. Therefore the respective column has no constraint: it may be updated and may be null.

- publisher_name is a derived attribute. Therefore it is not represented in the relational table.

### 17.2.1.1 Number sequence generator — 17.2 Object-relational mapping

Most database management systems provide number sequence generators that generate numbers that never repeat. This is necessary to provide values for primary keys, especially when multiple users are producing new records at the same time. The number sequence generator must assure that different users would not produce the same number at the same time.

Number sequence generators may be associated directly to the column of the table that contains primary keys. Every time a new record is inserted in the table, a new number in the sequence is created.

The database designer may choose an initial value for the sequence as well as an increment. For example, beginning with 500 with an increment of 5, the sequence generated would be 500, 505, 510, 515, etc.

### 17.2.1.2 Index selection — 17.2 Object-relational mapping

By default, a relational table is just a set of records. Finding a given object at a table would require iterating over all elements until the desired element is found. For example, looking for a book given its ISBN would require an exhaustive search that in average looks at half the table.

Databases usually provide, however, the possibility of indexing columns. An indexed column has an auxiliary table that allows specific records to be found in almost constant time. For example, if the isbn column of the table is indexed, then when a book is searched based on its ISBN, no iteration is performed over the set of all records: the system simply would translate the value of the ISBN into a position in memory by using a hash function and retrieve the element from that position. If that is not the desired element, then it looks for the next, and so on until finding it. If the hash function is well implemented and the hash table has enough space to avoid collisions (two values being translated to the same hash value), then usually the desired element is really in the first place searched, or very close to it at least.

The use of indices improves query speed. However, it slows database updating because every time a record is updated, inserted, or deleted, the auxiliary table must be updated as well (Choenni et al., 1993). Furthermore, indices also require more storage space for accommodating the auxiliary tables.

A primary key is indexed by default. Other columns may be indexed if the designer chooses to do that. Given the restrictions mentioned before, creating other indices may be an advantage in the case of an attribute that is used as internal qualifier. In that case, finding the objects quickly may be crucial for the application’s performance. Otherwise, indices should be avoided. For example, columns that are rarely used for searching purposes (e.g., a book’s page count) should not be indexed.

### 17.2.2 Associations — 17.2 Object-relational mapping

Generally, associations between classes correspond to associative tables in the relational model, that is, tables with a primary key composed of the primary keys values of the tables that represent the participating classes. In this case, each column of the primary key is said to be composed of foreign keys (fk) that are primary keys for other tables.

In this case, the primary key of the associative table is in fact composed of two (or more) columns. Each column may repeat values individually depending on the association multiplicity; but the pair (or tuple) of values that compound the primary key can never be repeated.

Depending on the multiplicity of the association roles, some rules must be observed. Many-to-many associations will have no individual unique restrictions. However, one-tomay associations require a unique restriction in one of the columns that form the primary key and one-to-one require a unique restriction in both columns that form the primary key. This is explained in further details in the following subsections.

### 17.2.2.1 Many-to-many associations — 17.2 Object-relational mapping

If the association is many-to-many with both role multiplicities defined as– * , then there is no restriction on the columns that compose the primary key of the associative table. Fig. 17–2 shows an example. The relational table for class Book is already represented in Table 17–1, and the relational representation of class Person is represented in Table 17–2.

**Figure 17–2: A bidirectional many-to-many association.** *(p. 353)*

> **Diagram content (transcribed from the figure image):** Many-to-many to table: Book (same attributes) * wish_list — * interested Person {«unique» «imm» +id: IdPerson; +name: String; «imm» +birth_date: Date} (bidirectional).

Notice that in Table 17–2 a customer has two unique columns: pk_person and id. The pk_person is a code generated internally to the system and unknown to the user. This column is also the primary key for this table. The other unique column is id, which may be some number that identifies this person and is known outside the system, such as the social security number.

Now, the many-to-many association of Fig. 17–2 can be represented as in Table 17–3 with a primary key composed of the fk of Book and Person. The unique restriction applies to both columns at once but not to them individually, and the not null restriction applies to each column individually.

Table 17–3 shows an associative relational table that represents the links between some people and some books. Notice that the pk spreads over two columns now. Each column contains a fk, that is, a value that corresponds to the primary key of another table.

In the associative table interested/wish_list, the columns fk_person and fk_book together form the composite primary key. Each one cannot be null individually, and pairs of fk_person/fk_book cannot be repeated. However, as the association is many-to-many, each individual column may repeat values, as seen in Table 17–3.

**Table 17–3: shows that Abe (person 20001) desires the books “Rama II” (10001) and “The Long Dark Tea-Time of the Soul” (10003), Beth (person 20002) only desires “Rama II” (10001), and Charles (person 20003) has no wishes.**

Instead of naming the associative table with the names of the classes (Person/Book), it is preferable to name it with the names of the roles (interested/wish_list), because more than one association may exist between two classes, and this way they will have different names.

**Table 17–2: Relational table for class Person.**

Table: Person

|pk,unique,imm,nn|unique,imm,nn|nn|imm,nn|
|---|---|---|---|
|pk_person|id|name|birth_date|
|20001|987–65-4320|Abe|01/04/1970|
|20002|987–65-4329|Beth|02/23/1982|
|20003|987–65-4325|Charles|12/05/1979|

**Table 17–3: Associative table representing a many-to-many association.**

|Table: interested/wish_list||
|---|---|
|pk, unique||
|nn|nn|
|fk_person|fk_book|
|20001|10001|
|20002|10001|
|20001|10003|

If the association is mandatory in one direction or both directions, then special considerations must be observed:

- If the association is mandatory on one side, then all primary keys from the other side must appear at least once in the associative table. If the role interested was mandatory * =

- (1..– ) in the example of Fig. 17–2, then each book should have at least one associated person as interested. Then, each primary key value from the Book table should appear in the interested/wish_list table at least once.

- If the association is mandatory on both sides, then all instances from both classes should appear at least once in the associative table. If in the example of Fig. 17–2, both roles were mandatory (1..– * ), then each book from the Book table and each person from the Person table should appear at least once in the associative table.

More generally speaking, considering that A has an association to B, and that the lower bound of the B role is n while the upper bound is m (multiplicity is n..m), the number of times that each instance of A must appear in the associative table is at least n, and no more than m. For example, if the multiplicity of role B is 2.5, then each instance of A must appear in the associative table at least twice and no more than five times.

### 17.2.2.2 One-to-many associations — 17.2 Object-relational mapping

When the association is one-to-many, then the column on the many side must have a unique constraint. This means that the column may not repeat elements individually while the other column in the composed primary key may repeat elements. The elements that cannot be repeated in the associative table therefore can be linked to a single element of the other table; this constraint assures that the association is one-to-many. Fig. 17–3 shows an example of a one-to-many association.

**Table 17–4: shows an associative table for the one-to-many association represented in Fig. 17–3. Notice that the unique constraint in the right column prevents the table from associating a book to more than one publisher.**

As seen in Table 17–4, publisher 30001 has one book (10002) and publisher 30002 has two books (10001 and 10003). As books cannot be repeated in this table, no book can be associated to more than one publisher.

**Figure 17–3: One-to-many association.** *(p. 355)*

> **Diagram content (transcribed from the figure image):** Many-to-one: Book * — 1 «imm» Publisher {«unique» «imm» +id: IdCompany; +name: String; +city: String}.

It is also possible to represent associations from many to one as fk in the table that represents the class at the many side of the association. For example, as each book may have only one publisher, then the association between book and publisher could be implemented as in Table 17–5.

The foreign key fk_publisher is a direct reference to the primary key of the Publisher table. If the association is straight to 1, then the foreign key column must not be null. If the association is to 0.0.1, then the foreign key column should not have that constraint.

Although this approach is not as homogeneous as associative tables, it is usually preferred by designers because it avoids the need to implement a new table. One disadvantage is that in this case, many-to-many associations are implemented as associative tables and many-to-one associations are implemented inside one of the original tables. Also, if the association is not mandatory (if its multiplicity is 0.1), and relatively few elements are associated, there would be lots of null values in the foreign key column, wasting storage space and degrading performance. However, if the association is straight to 1, this disadvantage does not apply.

**Table 17–4: Associative table representing a one-to-many association.**

|Table: publisher/book||
|---|---|
|pk||
|imm, nn|unique, nn|
|fk_publisher|fk_book|
|30002|10001|
|30001|10002|
|30002|10003|

**Table 17–5: An association being modeled as a single foreign key.**

|Table: Bo|ok|||||||
|---|---|---|---|---|---|---|---|
|pk, unique, imm, nn pk_book|unique, imm, nn isbn|imm, nn title|imm, nn authors_name|nn price|imm, nn page_count cover_image|nn quantity_in_stock|imm, nn fk_publisher|
|10001|0553286587|Rama II|Arthur C. Clarke and Gentry Lee|6.99|466|2|30002|
|10002|0553293370|Foundation and Empire|Isaac Asimov|5.99|282|3|30001|
|10003|0671742515|The Long Dark Tea-Time of the Soul|Douglas N. Adams|6.99|307|21|30002|

### 17.2.2.3 One-to-one associations — 17.2 Object-relational mapping

One-to-one associations, mandatory or optional, require that the associative table have a unique constraint in both columns of the composed primary key to prevent any element on both sides from appearing more than once in the associative table. Fig. 17–4 shows an example of one-to-one association that is mandatory on one side and optional on the other.

**Table 17–6: shows the relational table that implements the one-to-one association of Fig. 17–4.**

As the role is mandatory for payments, all instances of Payment must appear in the associative table, but not all instances of Order must appear, because the role is not mandatory for them.

As in the case of many-to-one associations, one-to-one associations may also be implemented as fk in one of the original tables. The foreign key column must necessarily be unique in that case. If the association role is also mandatory, then the foreign key column should not be null.

### 17.2.2.4 Ordered associations — 17.2 Object-relational mapping

An association with an ordered role (sequence or ordered set) may be implemented as an associative table with an extra column to represent the order of the element in the role’s collection of elements. Fig. 17–5 shows an example with two situations: ordered set and sequence (a list in which elements may be repeated).

**Figure 17–4: A one-to-one association that is mandatory on one side and optional on the other.** *(p. 357)*

> **Diagram content (transcribed from the figure image):** One-to-optional: Order 1 «imm» — 0..1 Payment (bidirectional).

#### Table 17–6 Associative table representing a one-to-one association.

|Table: order/payment||
|---|---|
|pk||
|imm, uniq, nn fk_order|uniq, nn fk_payment|
|50001|60001|
|50003|60002|
|50005|60003|
|50011|60004|
|50016|60005|
|50021|60006|
|50030|60007|

The difference between the relational implementation of an ordered set and a sequence is that in the case of the ordered set, the order column must not be included in the composed primary key, as shown in Table 17–7.

However, in the case of a sequence (elements may be repeated), the order column must be part of the composed primary key, which in this case is composed of three columns (Table 17–8).

**Figure 17–5: Ordered set and sequence.** *(p. 358)*

> **Diagram content (transcribed from the figure image):** Ordered and sequence associations: Book 1 «imm» — «ordered» «imm» 1..* Chaper (Chapter); Book * reserved — «sequence» * Person.

**Table 17–7: Relational table representing an ordered set.**

|Table: book/chapter|||
|---|---|---|
|Pk|||
|im,nn fk_book|im,unique, nn fk_chapter|nn order|
|10001|130001|1|
|10001|130002|2|
|10001|130003|3|
|10002|130004|1|
|10002|130005|2|
|10003|130006|1|
|10003|130007|2|

**Table 17–8: Relational table representing a sequence.**

|Table: book/customer|||
|---|---|---|
|pk|||
|nn fk_book|nn fk_customer|nn order|
|10001|20001|1|
|10001|20003|2|
|10001|20002|3|
|10001|20001|4|
|10002|20003|1|
|10003|20001|1|
|10003|20002|2|

In Table 17–8, the fact that the order column is included in the primary key allows the same person to reserve the same book more than once (e.g., 20001, Abe, has two reservations for book 10001, Rama II, in the first and fourth positions on the reservation list). A repetition like this would not be possible in Table 17–7, because the primary key does not include the order column: the same pair fk_book/fk_chapter cannot appear more than once in the table, regardless of its position.

In both cases, to prevent a given position to be occupied more than once, a unique constraint spreading over the origin class and the position should be defined. In the case of Tables 17–7 and 17–8, the pair fk_book/order should be unique.

### 17.2.2.5 Associations representing bags — 17.2 Object-relational mapping

In the case of bags, in which elements may be repeated but have no position, the usual solution is to add an extra column to the associative table with a counter for the number of times a given pair participates in the association. Fig. 17–6 shows an example of this kind of association.

**Table 17–9: shows the implementation of the associative table for the example in Fig. 17–6.**

Table 17–9 specifies that Abe (20001) has viewed the book “Foundation and Empire” (10002) six times. Beth (20002) viewed “Rama II” (10001) twice, “Foundation and Empire” (10002) once, and “The Long Dark Tea-Time of the Soul” (10003) once. It is not necessary to represent in the table any pair whose quantity is zero; this is why Charles (20003) does not appear in the table: he has never viewed any book.

### 17.2.2.6 Qualified associations — 17.2 Object-relational mapping

In the case of a qualified association defined as a map (multiplicity in destiny 1 or 0.1) with an internal qualifier (the qualifier is an attribute of the qualified class), it is sufficient to

**Figure 17–6: A bag.** *(p. 359)*

> **Diagram content (transcribed from the figure image):** Bag: Book * — «bag» * viewer Customer.

**Table 17–9: Associative table representing a bag.**

Table: book/viewer implement the association as a regular one-to-many or many-to-many association depending on the multiplicity on the side of the qualifier, as explained in previous sections.

|pk|||
|---|---|---|
|nn fk_book|nn fk_customer|nn quantity|
|10002|20002|1|
|10001|20002|2|
|10002|20001|6|
|10003|20002|1|

The only special care that the database designer must take in that case is to ensure that the column of the qualifier attribute is unique and immutable. It may be indexed if quick access to the records is necessary.

However, when the qualifier is external, it is necessary to add a third column to the associative table to allow for the representation of the qualifier. Fig. 17–7 shows an example of that situation.

Table 17–10 shows the implementation for the map defined in Fig. 17–7. The associative table has a primary key that is composed only of the origin class primary key and the qualifier. The destination class is left out of the primary key. However, it must be marked as unique because, in the example, each phone has a single type.

: If the external qualifier defines a partition (multiplicity– ), as shown in Fig. 17–8, it is implemented as shown in Table 17–10. But in the case of a partition with an external qualifier, the primary key must have three parts, including the origin and destination fk as well as the qualifier. Also, as the origin role multiplicity is 1, the destination class column must be marked with unique. In the example shown in Table 17–11, this means that a book may not have more than one genre.

If the role multiplicity at the origin were– (defining a relation where a book could have more than one genre), the implementation would basically be the same. The only difference is that the unique constraint in the destination column (fk_book) should not exist.

**Figure 17–7: Association with external qualifier.** *(p. 360)*

> **Diagram content (transcribed from the figure image):** Qualified map to table: Person with qualifier type 1 —× → 0..1 Phone {+area_code: AreaCodeNumber; +number: PhoneNumber}.

**Table 17–10: Associative table representing a map with external qualifier.**

Table: customer/phone

|pk|||
|---|---|---|
|nn fk_person|nn type|uniq, nn fk_phone|
|20001|Home|70001|
|20001|Cellphone|70002|
|20002|Home|70003|

**Figure 17–8: A partition.** *(p. 360)*

> **Diagram content (transcribed from the figure image):** Partition to table: Publisher with qualifier genre 1 —× → * Book.

### 17.2.2.7 Association classes — 17.2 Object-relational mapping

An association with an association class is represented in two parts: a relational table for the association class with its attributes, and an associative table for the association with a reference to the association class table. Fig. 17–9 shows an association class, and Tables 17–12 and 17–13 implement its relational equivalent.

Thus one way to represent associations with association classes is to use a table to represent the association class (Table 17–12), and an associative table (Table 17–13) with three columns: the primary keys of the participating classes (which form the composite primary key of the association) and the primary key of the association class, which is not part of the composite primary key of the association, but must be immutable and unique in that table.

**Table 17–11: Associative table representing a partition with external qualifier.**

|Table: publisher/book|||
|---|---|---|
|pk|||
|nn fk_publisher|nn genre|unique, nn fk_book|
|60001|sci-fi|10001|
|60001|sci-fi|10002|
|60002|humor|10003|

**Figure 17–9: An association class.** *(p. 361)*

> **Diagram content (transcribed from the figure image):** Association class to table: Person * employee — * employer Company with association class Job {+wage: Money; «imm» +hired: Date}.

**Table 17–12: Relational representation of an association with association class part one: the association class.**

|Table: Job|||
|---|---|---|
|pk, nn, imm, unique pk_job|nn wage|nn, imm hired|
|80001|1500.00|02/15/2008|
|80002|1200.00|03/01/1999|
|80003|2000.00|04/16/2005|
|80004|900.00|01/17/2001|

A further constraint is that all values for pk_job in the Job table must appear in the fk_job column of the employee/employer table.

### 17.2.2.8 n-ary associations — 17.2 Object-relational mapping

In the case of associations among three or more classes (n-ary), an associative table is defined in which the primary key is formed by the primary keys of all participating classes. Fig. 17–10 shows an example of a ternary association, and Table 17–14 shows its relational representation.

**Table 17–13: Relational representation of an association with association class part two: the association.**

Table: employee/employer

|pk|||
|---|---|---|
|nn|nn|nn, imm, unique|
|fk_person|fk_company|fk_job|
|20001|70001|80001|
|20001|70005|80002|
|20002|70001|80003|
|20003|70002|80004|

**Figure 17–10: A ternary association.** *(p. 362)*

> **Diagram content (transcribed from the figure image):** Ternary association BudgetItem * — FinancialYear * — Project * (central diamond) to be mapped to a table with three foreign keys.

**Table 17–14: association.**

#### Relational equivalent of a ternary

Table: BudgetItem/FinantialYear/Project

|pk|||
|---|---|---|
|nn|nn|nn|
|fk_budget_item|fk_financial_year|fk_project|
|90001|100001|110001|
|90001|100002|110002|
|90002|100001|110003|

In Table 17–14, pairs such as fk_budget_item/fk_project may repeat elements (90001/100001, for instance). But a triple such as fk_budget_item/fk_financial_year/fk_project should never repeat.

### 17.2.2.9 Façade controller associations — 17.2 Object-relational mapping

Some of the associations from the façade controller do not need to persist. Associations from the controller to all instances of a class, which are mandatory for the instances, do not need to be transformed into association tables, because, as the controller is also a singleton, they always repeat the same value for the controller column and have all the elements on the other side. That information is already available in the primary key column of the table representing the conceptual class, and, therefore, that association table would be redundant. For example, in Fig. 17–11, the association between the controller and Person via customer is mandatory for all people. Thus an associative table for representing that association would a primary key to the controller in one column and all primary keys of Person in the other column. As that information is already represented in the Person table, simply repeating them in a different table is unnecessary.

However, this observation is valid only if the association role is strictly 1 on the controller side. If the controller side has multiplicity 0.1, then the association should be represented separately. In Fig. 17–11, the premium_customer association must be represented somewhere because not every customer belongs to it. There are at least two choices for representing nonmandatory associations from the controller, for example, premium customers: adding a Boolean field to the Person table indicating which people are premium, or creating a single column table that contains the primary keys of premium customers.

The premium customer table does not have to include a column that represents the primary key of the controller because the controller is not an entity (and therefore it has no primary key), and because the controller is a singleton and even if a primary key is assigned to it, repeating the same value in all rows of the table would be unnecessary.

**Table 17–15: shows a possible implementation for this optional association.**

**Figure 17–11: A mandatory and optional associations from the controller façade.** *(p. 363)*

> **Diagram content (transcribed from the figure image):** Controller (singleton) associations: Control 1 —× → * customer Person and Control 0..1 —× → * premium_customer Person.

**Table 17–15: Implementation of an optional association from the façade controller.**

|Table: controller/premium|
|---|
|pk|
|nn, unique fk_customer|
|20001 20002|

According to Table 17–15, only Abe (20001) and Bea (20002) are premium customers, and Charles (20003) is not.

### 17.2.3 Inheritance — 17.2 Object-relational mapping

Relational databases do not support inheritance directly. Mapping inheritance relations to relational databases is an issue that demands attention. There are many different approaches, and this section discusses some of them. All examples in the following subsections are based on Fig. 17–12.

### 17.2.3.1 Implementing the entire hierarchy in a single table — 17.2 Object-relational mapping

One solution for representing inheritance that sounds straightforward at first glance is to implement the entire hierarchy in a single table. This table contains all the attributes of all classes in the hierarchy. It also has to identify which instantiated class is being represented in each record; this can be accomplished by adding a type column, as in Table 17–16.

Only attributes that belong to the class at the top of the hierarchy may not be null, because all other attributes could be null when the record belongs to one subclass and the attribute to another subclass. For example, if the type of the record is PromptPayment, then start_date and nr_of_installments must necessarily be null. If it is assumed that an object cannot change its class after instantiation, then the column type should be immutable.

**Figure 17–12: An example of inheritance.** *(p. 364)*

> **Diagram content (transcribed from the figure image):** Inheritance to tables: abstract Payment {+value: Money} with subclasses PromptPayment {+date: Date} and PaymentInInstallments {+start_date: Date; +nr_of_installments: [2..*]}.

**Table 17–16: Implementation of inheritance in a single table with a type field.**

|Table: Payment||||||
|---|---|---|---|---|---|
|pk, nn, unique, imm pk_payment|nn,imm type|nn value|date|start_date|number_of_installments|
|200001|PromptPayment|$300.00|04/09/2024|||
|200002|PromptPayment|$251.00|07/02/2024|||
|200003|PaymentInInstallments|$1890.00||12/09/2024|12|

**Table 17–17: Implementation of inheritance using one table for each concrete class part 1: PromptPayment.**

|Table: PromptPayment|||
|---|---|---|
|pk, nn, unique, imm|nn|nn|
|pk_prompt_payment|value|date|
|200001|300.00|04/09/2024|
|200002|251.00|07/02/2024|

**Table 17–18: Implementation of inheritance using a table for each concrete class part 2: PaymentInInstallments.**

Table: PaymentInInstallments

|pk, nn, unique, imm|nn|nn|nn|
|---|---|---|---|
| pk_payment|value|start_date|nr_of_installments|
|200003|1890.00|12/09/2013|12|

If multiple inheritance is used (e.g., if a payment could be prompt and installments at the same time),^4 then the type column should be replaced by a set of Boolean columns: is_prompt_payment and is_payment_in_installments. In this case, a payment could be prompt, in installments, or both (or neither, if they could also be instances of Payment, which in the present example cannot occur because Payment is an abstract class).

This approach has some disadvantages. It is hard to manage consistency between subclasses because all data are stored in the same place. Managing it adequately would require various complex control mechanisms. Also, lots of fields in the table would be null all the time, and the big table would be a very sparse one, especially if a big and complex hierarchy is being represented.

### 17.2.3.2 Each concrete class as a single table — 17.2 Object-relational mapping

Another approach to deal with inheritance is to represent each concrete class as a separate table. Each table would contain the attributes of the concrete class and the attributes of all its superclasses. Tables 17–17 and 17–18 show a possible implementation using that approach.

If only attributes are inherited, this approach may work. However, if superclasses define their own associations that must be inherited, then managing this becomes a headache because either an associative table should fill in data from different tables in a single column, or a single associative table should be implemented for each subclass that inherits the association.

4 Of course, this cannot be true. It’s just a supposition for the sake of the example.

### 17.2.3.3 Each class in a single table — 17.2 Object-relational mapping

A better choice for implementing inheritance given the aforementioned problems is to define one table for each class of the hierarchy, even the abstract ones. That way, attributes and association inheritance may be easily implemented. The main disadvantage is that for instantiating an object, a number of tables equal to the number of its superclasses plus one should be accessed. Tables 17–19 to 17–21 show how to implement this approach. There must be references from the subclasses’ tables to each immediate superclass table.

## 17.3 Saving and loading objects

*Chapter 17 · p. 366*

The equivalence between object-oriented design and the relational database is just part of the compatibility issues between these two paradigms. It is necessary also to decide how and when objects will be loaded and saved to the database. Some designers prefer to determine themselves the moment when such operations should be performed. However, that

**Table 17–19: Implementation of inheritance using a table for each class, part 1: Payment.**

|Table: Payment|||
|---|---|---|
|pk, nn, unique, imm|nn|nn|
|pk_prompt_payment|value|date|
|200001|300.00|04/09/2024|
|200002|251.00|07/02/2024|

**Table 17–20: Implementation of inheritance using a table for each class, part 2: PromptPayment.**

|Table: PromptPayment|||
|---|---|---|
|pk, nn, unique, imm pk_prompt_payment|nn, unique, imm fk_payment|nn date|
|300001|200001|04/09/2024|
|300002|200002|07/02/2024|

**Table 17–21: Implementation of inheritance using a table for each class, part 3: PaymentInInstallments.**

|Table: PaymentInInstallments||||
|---|---|---|---|
|pk, nn, unique, imm|nn, unique, imm|nn|nn|
|pk_payment_in_installments|fk_payment|start_date|nr_of_installments|
|400001|200003|12/09/2023|12|

handcrafted approach for saving and loading objects is subject to logic errors and usually may pollute the domain-level code.

In addition, if the decision when to save and load objects is taken manually, sometimes those operations can be performed without necessity (e.g., loading objects that are already in memory and saving objects that were not changed). Controlling these issues case by case is not the most agile way to develop software.

It is possible to implement the processes for saving and loading objects with automatic mechanisms. In this case, the designer should only decide which classes, attributes, and associations are persistent, and a whole set of methods and data structures will be automatically created to allow those elements to be loaded and saved at the appropriate moments. Initially, this section presents the basic or naïve implementation of this mechanism. Later, the limitations of the technique are explained, and possible solutions drafted.

### 17.3.1 Virtual proxy — 17.3 Saving and loading objects

In order to implement an automatic mechanism for saving and loading objects, we can use a design pattern called virtual proxy (Gamma et al., 1995). A virtual proxy is a very simple object that implements only two responsibilities:

- It must know the value of the primary key of the real object it represents.

- It must redirect to the real object all messages it receives in its name.

Below is a draft of the way a virtual proxy works:

**from broker import * class VirtualProxy: def __init__(self, an_real_object_pk): self.real_object_pk = an_real_object_pk def __getattr__(self, name): real_object = BrokerManager.get_real_object(real_object_pk) def method(*args, **kwargs): if hasattr(self.real_object, name): return getattr(self.real_object, name)(*args, **kwargs) else: return self.execute(name, self.real_object, args, kwargs)**

The logic behind the virtual proxy is that one of its instances will intercept any message sent to another object through an association link. The proxy will call, then, a broker that may be one for a system or one per class, in order to locate the real object and send it back to the proxy. If the broker finds that the object is in main memory (inside one of the caches), then it will simply send to the proxy a link to the real object. If the object is not in memory, then the broker will locate it in the database and load it to a clean cache. Finally, if the object has this message implemented, then it is executed. Otherwise, an exception will be raised.

**Figure 17–13: Two instances, (A) before and (B) after calling an object that is not in memory.** *(p. 368)*

> **Diagram content (transcribed from the figure image):** Lazy loading with proxies: (A) :Publisher linked to three :BookProxy objects holding only pk = 10001, 10002, 10003; (B) after one book is loaded, :Publisher → BookProxies and a real :Book (pk 10002) whose chapters are still :ChapterProxy objects pk = 30004, 30005.

Later, in the following sections, the way the BrokerManager works is gradually explained.

Thus the design with virtual proxies requires that instead of associating domain objects directly with other domain objects, they must be associated to their proxies. In this way, it is possible to bring into memory an instance of Publisher without loading all instances of Book that are linked to it. The instance of Publisher is associated to the proxies of books, which are very simple objects. The proxies are created in main memory and require much less space than the instances of the real class, such as those of Book. An instance of Book is loaded only if necessary, that is, only if a message is sent to it through its proxy. This economic way of using memory is called lazy load, and it is very efficient in terms of time and main memory in some situations.

To prevent the designer from worrying about when the objects must be loaded, the virtual proxy mechanism must be interposed to all persistent links in main memory. Real objects send messages to each other as if the proxies did not exist. But proxies intercept every message. The proxies ensure that the real object will be loaded if it is not in memory.

Fig. 17–13 is an example of the lazy load mechanism. Initially (A), only one instance of Publisher is in main memory. It is associated to three books. However, instead of having the books in memory, only their proxies are there. If the instance of Publisher must send a message to one of the books, it simply sends the message through the link; the message is intercepted by the proxy that calls the BrokerManager, which ensures that the book is loaded into the memory (B). As the book is associated to some chapters, only the chapters’ proxies are created in memory, not the real objects.

If one of the chapters receives a message from the book, then only that chapter would be brought into memory.

### 17.3.1.1 Virtual data structures — 17.3 Saving and loading objects

The implementation of virtual proxies for each object may be inefficient when an object has many links; for example, a publisher with 50,000 registered books would demand the instantiation of 50,000 proxies to be associated to it when it is brought into memory. Fortunately, there is a way to avoid instantiating large quantities of proxies, which is the implementation of virtual data structures to physically replace the implementation of the associations in main memory.

Thus an instance Publisher would not have 50,000 links to 50,000 proxies of Book, but a single link to a VirtualSet structure with 50,000 PKs to books. The VirtualSet implements usual operations to add, remove, update, and query objects: the same operations that a normal set implements. The only difference is that it does not store the real objects, but only their primary keys. The virtual set does not bring objects into memory; it brings only their primary key numbers. The VirtualSet and its counterparts, VirtualSequence, VirtualOrderedSet, VirtualBag, VirtualMap, etc., use the BrokerManager to load real objects when necessary, instead of holding all the real objects.

A virtual data structure may be implemented with the following principles:

- Instead of a physical representation of a collection of objects, it is a physical representation of a collection of the primary key values of the real objects.

- The method that adds an object to the collection must only add the primary key of the real object to the physical representation.

- The method that removes an object from the collection must only remove the primary key of the real object from the physical representation.

- Any method that performs a query on the data structure to return one or more objects receives the real object(s), which are requested from the broker manager.

Thus adding and removing links between objects may be performed without having the real objects in memory (at least from one side of the link). An object is only brought into memory when information about it becomes necessary, that is, when it receives a message.

### 17.3.1.2 Lazy load — 17.3 Saving and loading objects

Lazy load is useful because it only brings into memory objects that are going to receive a message. For example, if an instance of Publisher is in main memory and one of its books is going to be updated, then it is not necessary to load all instances of Book linked to the publisher, but only one.

On the other hand, if the instance of Publisher must search its books to find the most expensive of them, then all instances of Book that are linked to it must be loaded into main memory. This is the drawback of the technique. Performing all operations on objects in main memory can be an extraordinary waste of time. Imagine loading 50,000 instances of books to main memory just to discover which one of them has the highest price.

One possible solution would be modifying the virtual proxy class to allow it to bring into memory not only the primary key of the object, but a subset of its attributes as well. In order to find the highest priced book, a virtual set would contain pair of primary keys and price. Thus the higher price can be found without loading any complete book into main memory.

Virtual proxies work well when relatively few objects are brought into memory for each user operation. For example, a user searching for books to buy will only view a relatively small quantity of books in the list. That user would operate over just a single shopping cart and order. Those kinds of operations over small sets of objects are perfectly handled automatically by virtual proxies. However, when queries or commands involve iterating over large collections of objects, such as increasing the price of all books in the store, then using virtual proxies should be avoided, unless wasted processing time is not a problem; but that usually is not the case.

Thus for performing queries or commands over large collections of objects, if the query or command uses just a few attributes of the objects, it would be advisable to consider replacing the virtual proxy mechanism in that specific case by a query or command directly performed over the database. Therefore some messages, when they reach specific objects, would be redirected to a specific encapsulated implementation that performs the necessary actions in the database and returns the results as necessary, rather than being redirected to a proxy.

### 17.3.2 Brokers and materialization — 17.3 Saving and loading objects

The process of loading an object from the database into main memory is called materialization. Materialization is usually requested by a proxy to a broker manager, which may in turn delegate materialization to a specialized broker. The broker manager looks if the requested object is in main memory. If it is not, then the broker manager activates the specialized broker to materialize the object.

Each class may have its own specialized broker. However, a single broker may also be implemented to serve all classes. A specialized broker must implement a method called materialize that does the following:

1. It creates in main memory an instance of the persistent class.

2. It initializes the values of the attributes of the new instance with values taken from the respective line and columns in the database.

3. It loads and initializes the virtual data structures that implement the associations of the object with the primary keys of the respective linked objects.

In order to obtain the values for the primary keys of the linked objects, the specialized broker must know what associations are attached to the object being loaded; then it searches the occurrences of the primary key of the object in the associative tables that implement those associations. The primary keys of other objects associated to the primary key of the object being materialized are added into the virtual data structure, which has the responsibility of holding the respective association.

For example, an implementation of a broker for the class Book, Broker4Book should materialize instances of Book, as defined in Fig. 17–14.

**Figure 17–14: A conceptual model for books and their chapters.** *(p. 370)*

> **Diagram content (transcribed from the figure image):** Composition: Book (full attributes) 1 ◆ «imm» —× → «imm» 1..* Chapter {«imm» +number: Natural; «imm» +title: String; «imm» +contents: String}.

According to this conceptual model, Broker4Book must implement the materialize method by performing the following operations:

1. Create an instance of Book.

2. Fill in the isbn, title, authors_name, price, page_count, cover_image, and quantity_in_stock attributes of the new instance with the values stored in the respective columns of the Book column in the database.

3. Search the book_chapter table for occurrences of the primary key of the book in the fk_book column. For every occurrence, add the corresponding value found in the fk_chapter column to the virtual set chapters of the new instance of Book, which implements the association role for the book.

The materialization performed by the specialized broker must not be confused with the creation of a new instance as defined by the system operation contracts. In the contracts, the creation of an instance refers to the insertion of new information in the system, independent of the physical storage (main memory or secondary memory). The materialization performed by the broker only refers to the operation of bringing into the main memory an existing object that is not there physically yet. Materialization is, therefore, an operation that belongs exclusively to the persistence tier; it has nothing to do with the business tier.

### 17.3.3 Caches — 17.3 Saving and loading objects

Objects in main memory may be classified as follows regarding their state related to the database:

- Clean or dirty, depending on whether they are consistent with the version stored in the database.

- Old or new, depending on whether they already exist in the database or not.

- Deleted or kept, depending on whether they have been deleted in main memory but not yet deleted in the database.

A cache is a data structure similar to a map or dictionary that associates primary key values to the real objects they represent.

Although there are eight possible combinations for the features defined above, in practice only four combinations are sufficient to manage objects in main memory:

- Old clean cache: Keeps objects that are in main memory and consistent with the database.

- Old dirty cache: Keeps objects that are in main memory and in the database, but that have been updated only in main memory and, therefore, are inconsistent with the database.

- New cache: Keeps objects that have been created in main memory, but which are not yet in the database.

- Delete cache: Keeps objects that were deleted in memory, but still exist in the database.

The broker manager verifies that an object is in main memory by performing a query on the existing caches, asking for the primary key of the object being requested. If the broker manager finds a reference to that object in one of the caches, it returns the reference to the proxy that asked for it. On the other hand, if the broker manager does not find any reference to the requested object in any cache, then it asks a specialized broker (as, e.g., Broker4Book) to materialize the object. The object is then materialized and inserted into the old clean cache.

If, after that, the object is updated in main memory, it must be moved to the old dirty cache.

The persistence mechanism must have ways to assure that every time the inner state of an object in the old clean cache is changed, it is moved to the old dirty cache. This could be accomplished, for example, by adding a special command such as BrokerManager.become_dirty(self) to any method that changes the object. If the object originally is in the old clean cache, that method will move it to the old dirty cache.

Objects that were created in memory as a result of a contract postcondition are stored into the new cache. An object that is in the new cache may not be moved to the old dirty cache, even if its attributes are changed. It stays in the new cache until a commit is performed. After the commit, it is moved to an old clean cache.

When an object is deleted from main memory, the result will depend on which cache the object came from. If it was in the old clean cache or in the old dirty cache, then it is moved to the delete cache. However, if it was in the new cache, then it may be simply deleted from main memory.

### 17.3.3.1 Commit and rollback — 17.3 Saving and loading objects

The commit and rollback operations are usually activated by the interface tier to indicate that a transaction was successful and confirmed, or that it was canceled, respectively. These operations are implemented by the broker manager. In the case of a commit, the broker manager should do the following:

1. Perform an update in the database for every object in the old dirty cache and move those objects to the old clean cache.

2. Perform an insert in the database for every object in the new cache and move those objects to the old clean cache.

3. Perform a remove in the database for every object in the delete cache and delete those objects from main memory.

In the case of a rollback, the broker manager must simply remove all objects from all caches, except those in the old clean cache.

As the old clean cache may grow indefinitely, it is necessary to implement some mechanism to remove the oldest objects from it every time its size reaches some previously established threshold.

The other caches only grow up-to-the-moment a commit or rollback is performed. At that moment, they are emptied.

### 17.3.3.2 Cache control in a multiuser server — 17.3 Saving and loading objects

If more than one user connects to the system, it is necessary to determine how to share objects among different users. Assuming we have a client/server architecture with interface, domain, and persistence tiers, at least two approaches are possible:

- The three tiers are executed in the client. There is no main memory share in the server, only the database. The client is heavy, and the server is used only to access or store data after a commit is performed. In this case, what travels in the network is data in the form of relational table records and SQL^5 instructions. Information travels only when an object must be materialized or committed. The disadvantage of this design is that the client node is overloaded. However, client applications have recently become richer and more complex. Not depending on a server to process the logic of the application may be the best option.

- The domain and persistence tiers are implemented in the server, and only the interface tier is implemented in the client. In this case, the objects will exist in main memory only in the server, and what travels through the network are the parameters of the system operations and the returns from queries, usually in the form of DTOs. The advantage is that clients are lighter, and usually it may be cheaper to upgrade a server than upgrading thousands of clients. However, for some applications that require fast processing of the data, waiting for a busy server may not be viable.

If the objects are physically in the server only, there are still more possibilities. One that must be ruled out is to allow all users share the four caches. It has the disadvantage that a user could have access to objects that are being modified, created, or deleted but have not yet been committed by another user. This option seems to be unadvisable for most applications.

The other option is to share only the objects in the old clean cache among the users. There should be multiple instances of other three caches that are private to each user. If an object is in a private cache of one user, then the other users cannot access it. They must wait for a commit or rollback from the first user. Thus the persistence mechanism for multiuser access could be implemented like this:

- An old clean cache is shared by all users.

- Each user has a private old dirty cache, delete cache, and new cache.

By doing this, it is possible to ensure that no user would have access to objects that are being modified by other users. Therefore it is possible to use the caches to implement a lock mechanism, that is, when a user is updating an object, the other users cannot access it. Only when the user that has the object performs a commit or rollback, and the object is moved to the old clean cache or cleaned from main memory, can the other users gain access to it again.

> *Footnote 5:* Structured Query Language, the dominant language for defining, accessing, and updating relational databases (Date, 1982).

An advantage of this method is the optimized usage of main memory. All users share the objects in the old clean cache, which is the only one that grows indefinitely. The other four caches, which are specific for each user, only grow during a transaction. When a commit or rollback happens, those caches are emptied.

However, this may negatively affect scalability, because some users could be stuck while others are dealing with some objects. It is possible to implement a more sophisticated control mechanism based on optimistic merges: two or more users may edit the same object as long as they do not update the same attribute or association.

This must be used with care, however. Concurrency issues may be rather complicated concerns, and many decisions may depend on business rules. For example, may the price of a book be updated while a user is finishing an order?

Some applications could even require a more pessimistic locking strategy: if a user is browsing an object, no other user may even have access to view it. This is the case for banking applications, for example, which require maximum data security.

## Questions (Chapter 17)

1. What kind of associative table should be used to represent an association that is ordered in both directions? How do you represent it in the case of two ordered sets, or two sequences, or one ordered set and one sequence?

2. What kind of association table should be used to represent an association with an association class that is marked with {bag} on one side?

