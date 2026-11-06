<!-- Knowledge file: Chapter 11 — Conceptual modeling: patterns -->
> **About this file.** Chapter 11 of a cleaned, AI-ready edition of Wazlawick, R. S. (2024). Object-Oriented Analysis and Design for Information Systems: Agile Modeling with BPMN, OCL, IFML, and Python (2nd ed.). Morgan Kaufmann/Elsevier. ISBN 978-0-443-13739-6.  
> **Covers:** Analysis patterns: high cohesion, specification classes, quantity, measure, strategy, composite, organizational hierarchy, object joining, account/transaction, range/interval, temporal patterns (history, temporal, bitemporal).  
> **Use this file when:** solving a recurring domain-modeling problem (units, measurements, discounts, hierarchies, histories, ledgers, intervals).  
> **Sections:** 11.1 Introduction to conceptual model patterns (p. 177); 11.2 High cohesion^1 (p. 177); 11.3 Specification classes (p. 184); 11.4 Quantity (p. 185); 11.5 Measure (p. 188); 11.6 Strategy (p. 190); 11.7 Composite^2 (p. 192); 11.8 Organizational hierarchy (p. 194); 11.9 Object joining (p. 197); 11.10 Account/transaction (p. 201); 11.11 Range or interval (p. 208); 11.12 Temporal patterns (p. 210); 11.13 Discussion (p. 215)  
> **Contains:** 54 figures transcribed as text, 10 code listings.

# Chapter 11: Conceptual modeling: patterns

*Source: Wazlawick, Object-Oriented Analysis and Design for Information Systems, 2nd ed. (Elsevier, 2024), starts p. 177*

## Key topics in this chapter (Chapter 11)

- High cohesion

- Specification classes

- Quantity

- Measure

- Strategy

- Composite

- Organizational hierarchy

- Account/transaction

- Interval

- Temporal patterns

## 11.1 Introduction to conceptual model patterns

*Chapter 11 · p. 177*

Class diagrams that represent conceptual models almost always become more complex and harder to maintain than the team members would like. Naïve models may be unnecessarily complex. Fortunately, there exist techniques that reduce the complexity of such diagrams and, at the same time, improve their expressiveness.

These techniques are called analysis patterns and may be understood as a special case of design patters (Gamma et al., 1995) that are applied specifically to the conceptual model. Most patterns presented in this chapter were first described by Fowler (2003) and are here adapted to the UML notation and, sometimes, evolved.

Analysis or design patterns are not rules that must be obeyed, but recommendations based on previous experience. It is the responsibility of the analyst to decide when to apply a given pattern in the models.

## 11.2 High cohesion^1

*Chapter 11 · p. 177*

High cohesion is so important for object-oriented modeling that it is considered more a principle or guideline axiom than a pattern itself. A concept with high cohesion is more stable and reusable than a concept with low cohesion, which can become rapidly confusing and hard to maintain. Most systems could have all their information represented in a single table, but that would be an extreme worst case of low cohesion, and it would not be practical.

> *Footnote 1:* Usually, high cohesion is mentioned in conjunction with low coupling. However, as coupling problems appear to emerge when object collaborations are designed, discussion on low coupling is left for a further chapter. 

179

Almost every metric for class cohesion needs to compare attributes and methods (Miquirice and Wazlawick, 2018), and therefore, they may not be used during conceptual modeling, because methods are still missing from the model. In this chapter, however, we present not a metric, but a set of clues that may indicate that a class, even without its methods, is already suffering from cohesion problems.

Earlier, we mentioned that concepts should not have attributes that belong to other concepts (e.g., a car should not have the owner’s ID as one of its attributes). Attributes also must not have class names or data structures (set, list, array, etc.) as data types because all those situations lead to low cohesion. A class with that kind of attribute is probably representing more than one single concept. For example, an instance of Order should not have an items_list attribute because items have their own attributes and associations; they should appear related to Order by a 1 to – association.

If a Person can have more than one address, instead of the naïve solution of creating attributes such as address1, address2, or even address:Array , String., we should create a new concept (Address), which is associated to Person. Imagine how hard it would be to deal with the transformation of the single string address to a complex concept with attributes number, street, city, state, etc., if the addresses were modeled as multiple attributes or as an array of strings such as in Fig. 11–1.

The same Fig. 11–1 shows how to represent this concept by separating Person’s attributes and Addresses.

Concepts and attributes should have a simple structure with high cohesion elements. Evidence of low cohesion includes scenarios where some attributes of a class may be null depending on the value of other attributes. If complex constraints (invariants) are necessary to keep a concept consistent, this is equivalent to using duct tape to keep the pieces of a broken pot together.

**Figure 11–1: Naïve ways of representing addresses and a better way with more cohesion.** *(p. 180)*

> **Diagram content (transcribed from the figure image):** High cohesion — multivalued attribute. AVOID ("these two options lower the cohesion of class Person"): Person {+id; +name; «opt» +address1, +address2, +address3: String} and Person {+id; +name; +address: OrderedSet(String)}. BETTER ("a separated class for a multivalued attribute"): Person {+id: ID; +name: String} * — * {ordered} Address {+location: String}, which easily evolves into Address {+number: Natural; +street: String; +city: NamesOfCities; +state: NamesOfStates; +country: NamesOfCountries}.

In Fig. 11–2, the attributes paid_value and payment_date are mutually dependent: either both are null, or both are not null. An invariant was added to the class to avoid the situation where one of them is null while the other is not, in order to avoid inconsistent instances. Invariants are good to represent business rules that must always be valid. But when an invariant just relates two attributes of a class like in this example, it is a strong clue of lack of cohesion.

A better way to model this situation is shown in Fig. 11–3, where the concepts Order and Payment appear separated but with high cohesion each one. In this case, there are no optional attributes depending on each other and no need for constraints.

Another potential problem related to low cohesion is the existence of groups of strongly correlated attributes, as seen in Fig. 11–4 where it can be observed that groups of attributes have stronger relations among them then outside the group. It happens to attributes such as street, number, city, and state, which together compose an address, or ddd (distance direct dialing) and phone, which are part of a complete phone number, or passport_number and issuing_country, which are part of passport information. In this figure, we have even used lines to divide the groups of strongly related attributes, but remember that this is not an UML notation, it is just a way to help in observing groups that are implicit in the set of attributes of the Order class.

The relation that exists inside each group appears implicitly in the position they are placed in the class description. This is bad, because if the attributes are moved from their original position, by being alphabetically sorted, for example, the weak structure of the groups would be messed up. The alphabetic order would be city, ddd, issuing_country, name, number, passport_number, phone, state, and street (see Fig. 11–5). Now it is harder to comprehend which attributes are related to address, or phone number or passport, because they are mixed up, and no notation helps in knowing their weak relations. The understanding of the attributes of a concept should not depend on the ways those attributes are sorted.

**Figure 11–2: A class with low cohesion because attributes depend on each other.** *(p. 181)*

> **Diagram content (transcribed from the figure image):** AVOID ("attributes that depend from other attributes hinder the class cohesion"): Order {not payment_date->isNull() xor paid_value->isNull()} with «imm» +due_value: Money, «imm» +due_date: Date, «opt» +paid_value: Money, «opt» +payment_date: Date.

**Figure 11–3: Modeling solution with high-cohesion classes.** *(p. 181)*

> **Diagram content (transcribed from the figure image):** Better: Order {«imm» +due_value: Money; «imm» +due_date: Date} 1 —«imm»— 0..1 Payment {«imm» +paid_value: Money; «imm» +payment_date: Date}.

**Figure 11–4: A class with low cohesion because of subgroups of strongly related attributes.** *(p. 182)*

> **Diagram content (transcribed from the figure image):** AVOID ("a class with low cohesion"): Person with groups of attributes {«imm» «unique» +id: ID; +name} / {+street: StreetName; +number: Natural; +city: CityName; +state: StateName} / {+ddd: DDDCode; +phone: PhoneNumber} / {+passport: PassporNumber; +issuingCountry: CountryName}.

**Figure 11–5: A class with attributes alphabetically sorted, which hinders comprehension.** *(p. 182)*

> **Diagram content (transcribed from the figure image):** The same low-cohesion Person with attributes listed in arbitrary order (city, ddd, id, issuingCountry, name, number, passport, phone, state, street) — groups are hard to see.

A better solution to improve high cohesion in that model is shown in Fig. 11–6. This solution also eases the way to other modeling possibilities such as allowing a person to have more than one address or more than one phone or passport. In those cases, it is simply necessary to change the association role multiplicity.

Yet another situation occurs when some attributes repeat their values for a group of instances. Fig. 11–7 presents an example. In this figure, the attributes customer_name, costumer_id, and customer_birth_date repeat the same values for different orders when the customer is the same and has not changed her name, which is an extraordinarily rare situation.

**Figure 11–6: A model with classes with high cohesion.** *(p. 183)*

> **Diagram content (transcribed from the figure image):** Refactored: Person {«imm» «unique» +id: ID; +name: String}; Person * — 1 Address {«imm» +number: Natural; +street: StreetName; +city: CityName; +state: StateName}; Person 1 —«imm»— 1 Passport {«imm» +passport: PassporNumber; «imm» +issuing_country: CountryName}; Person * — 1 Phone {«imm» +ddd: DDDCode; «imm» +phone: PhoneNumber}.

**Figure 11–7: A class with low cohesion because it has attributes that repeat for a given set of instances.** *(p. 183)*

> **Diagram content (transcribed from the figure image):** AVOID ("there are attributes that depend from an attribute that is not unique"): Order {«imm» «unique» +number: Natural; «imm» +date; «imm» +due_date; «imm» +due_value: Money; «imm» +costumer_id: ID; +costumer_name: String; «imm» +costumer_birth_date: Date}.

**Figure 11–8: A model with higher cohesion than the one in the last figure.** *(p. 183)*

> **Diagram content (transcribed from the figure image):** Refactored: Order {«imm» «unique» +number; «imm» +date; «imm» +due_date; «imm» +due_value} * — 1 customer Person {«imm» «unique» +id: ID; +name: String; «imm» +birth_date: Date}.

In database theory, we could say that in this case, the class has attributes that depend on another attribute that is not a candidate key. Namely, costumer_name and costumer_birth_date both depend on costumer_id, and this last attribute is not unique for this class and therefore, not a candidate key.

This type of situation can be eliminated by splitting the concept into two associated concepts with better cohesion, as shown in Fig. 11–8. Notice that even attributes’ names are shortened with this choice of model because they are not anymore misplaced attributes referring to another concept.

## 11.3 Specification classes

*Chapter 11 · p. 184*

A special case of low cohesion happens when an object is confused with its specification. That situation is very frequent: sometimes, products or physical items share a common specification, while their exemplars may have some differences among them.

One example of specification is the difference between the concept of a book as a published title and a book as a physical copy of a published title. If both book concepts are not distinguished, lots of trouble will occur.

The class Book may refer to the published title, while BookCopy may stand for the physical copies. Thus an instance of Book is a specification for a set of instances of BookCopy, as seen in Fig. 11–9.

Depending on the information needs, it would be necessary to differentiate one copy from another. For example, if used books are to be sold, the conservation state should be kept for each copy. In this case, the Book class could be used as a specification for the class BookCopy, whose instances are single copies of a book.

The specification class Book should contain the attributes and associations that do not vary for different copies of the same book. For example, different copies of the same book have the same title, author, ISBN, base price, etc. However, conservation state and discount may be distinct for each copy. Thus these attributes (and associations, if any) are placed in the BookCopy class.

It is possible for a class to have more than one specification. For example, the discount of the book could be predetermined depending on the conservation state of the book (an enumeration with values such as new, used, damaged, etc.). Thus a copy, besides being specified by the published title, may be specified by its state of conservation. Thus Conservation would be a class with some instances that will associate the conservation state of any book with a predetermined discount. For example, all new books may have 0%, all used books, 10% and all damaged books 50%. This new situation is shown in Fig. 11–10.

The instances of class Conservation have two attributes. The first is the conservation state, which is a value obtained from the enumeration ConservationState. There are initially only three possible values: new, used, and damaged, which means that this class may only have three instances at maximum. The second attribute is the discount percentage that would be applied to a copy depending on its conservation state. As it is expected that books with the same conservation state have the same discount, then the attribute state in class Conservation must be unique.

**Figure 11–9: A class and its specification.** *(p. 184)*

> **Diagram content (transcribed from the figure image):** Specification class pattern: Book {«imm» «unique» +isbn: ISBN; «imm» +title; «imm» +author; +price: Money} 1 specification «imm» — * copies BookCopy {+state: ConservationState; +discount: Percentual}; «enumeration» ConservationState {new, used, damaged}.

**Figure 11–10: A class with two orthogonal specifications.** *(p. 185)*

> **Diagram content (transcribed from the figure image):** Double specification: Book (literary_specification, «imm») 1 — * copies BookCopy; BookCopy * — 1 conservation_specification Conservation {«imm» «unique» +state: ConservationState; +discount: Percentual}; «enumeration» ConservationState {new, used, damaged}.

**Figure 11–11: A class where a quantity is expressed by a predefined unity.** *(p. 185)*

> **Diagram content (transcribed from the figure image):** Book {«imm» «unique» +isbn; «imm» +title; «imm» +author; +price: Money; +weight: Pound} — a quantity hard-wired to one unit.

If that attribute was not unique, then the class Conservation could have any number of instances and different values of discount could be associated with the same conservation status.

## 11.4 Quantity

*Chapter 11 · p. 185*

Frequently, the team faces the need to model quantities that are not merely numbers. For example, the weight of a book could be defined as 400. But 400 what? Grams? Pounds? Kilos? One solution is to define a specific type for the weight (Pound, for example), and then keep using it consistently. The attribute then could be declared as weight:Pound as seen in Fig. 11–11. But that demands that all books have their weight expressed in pounds.

In some cases, however, the system must be configurable to support different weight units. In some countries, grams and kilograms are used, while others use pounds, or even other units. If the attribute has a type that refers to a specific unit, then the system should suffer refactoring to accommodate new weight units.

However, the Quantity pattern allows different unit systems to coexist and to be easily exchangeable. The pattern consists of creating a new primitive type named Quantity, which has two attributes, value and unit, as shown in Fig. 11–12.

**Figure 11–12: An example of use of pattern Quantity.** *(p. 186)*

> **Diagram content (transcribed from the figure image):** Quantity pattern: Book {…; +price: Money; +weight: Quantity}; «primitive» Quantity {+value: Real; +unit: Unit}; «enumeration» Unit {gram, pound, kilo}.

**Figure 11–13: Different kinds of specialized units.** *(p. 186)*

> **Diagram content (transcribed from the figure image):** Parameterized quantity: Book {«imm» «unique» +isbn; «imm» +title; «imm» +author; +price: Quantity<MoneyUnit>; +weight: Quantity<WeightUnit>; +height: Quantity<SizeUnit>; +width: Quantity<SizeUnit>}; «primitive» Quantity<Type> {+value: Real; +unit: Type}; enumerations WeightUnit {gram, pound, kilo}, MoneyUnit {Dolar, Euro, Real, Yen, Yuan}, SizeUnit {centimeter, inch, meter, yard}.

This way, the weight of each book is specified as a primitive quantity formed by a numeric value and a unit, whose type is an enumeration with possible values defined as grams, pounds, and kilos.

### 11.4.1 Different units — 11.4 Quantity

If different kinds of measures are necessary, then the units may be specialized, for example, time units, weight units, and size/distance units. One example is shown in Fig. 11–13.

In this figure, we introduce the concept of genericity or generic class, which is the case of class Quantity that can be instantiated necessarily with an existing type being bound to the parameter “Type.” For example, Quantity , SizeUnit . is instantiated with attribute unit being typed with SizeUnit, which replaces Type. In this example, besides defining WeigthUnit and SizeUnit respectively to represent the weight of a book and its dimensions, we take the liberty to internationalize the price attribute of Book, by using Quantity , MoneyUnit . as type (let us assume that the user demanded that).

### 11.4.2 Unit conversion — 11.4 Quantity

If a unit conversion is needed, then an option is to use a new class QuantitySpecification that has a qualified association to the new class Ratio. This is an interesting kind of qualifier because the instance of Ratio is qualified by a derived attribute destiny_unit, which belongs to the class QuantitySpecification, but that is accessed by a different association (destiny). See Fig. 11–14 for more details.

From the point of view of the class Ratio, it has two associations with multiplicity 1 to the class QuantitySpecification. One is origin and the other is destiny. The class Ratio also has an attribute called divider. Its meaning is the following: the unit type in origin can be converted to the unit type in destiny if the value related to origin is divided by divisor. For example, if the origin is kilometer and the destiny is meter, then the divider must be 1000. More specifically, 5500 m divided by 1000 are equal to 5.5 km. Notice that there must exist an instance of Ratio, which is linked to origin kilometer and destiny meter and with divisor 1000.

Those ratios may be also used in OCL expression. Suppose that we want to return the value of the attribute distance from some class and necessarily converting it to kilometers (does not matter the original unit in which it is recorded), we could write an expression like this:

```ocl
Context Anyclass::distance_as_kilometers(an_object):Float
    body:
        an_object.distance.value /
        an_object.distance.unit.destiny_unit[kilometers].divider
```

Here, Anyclass::distance_as_kilometers is the class and query we are defining. It returns a float number that we expect to be in kilometers. The argument an_object that is received should have an attribute named distance and its unit may be anyone, but hopefully a DistanceUnit. We can access the correct Ratio instance that converts any existing type of

**Figure 11–14: An extension of pattern Quantity with conversion ratios.** *(p. 187)*

> **Diagram content (transcribed from the figure image):** Quantity with conversion ratios: Quantity {+value: Real; +unit: QuantitySpecification}; «primitive» QuantitySpecification<Type> {+unit: Type}; QuantitySpecification 1 destiny — * destiny_ratio Ratio and 1 origin — * origin_ratio Ratio (qualified by destiny_unit: Type); Ratio {destiny.classifier == origin.classifier} {+divider: Float; +/destiny_unit: QuantitySpecification = self.destiny…}; enumerations SizeUnit, MoneyUnit, WeightUnit; note: x = Quantity.new(); x.value/unit[meter].divider (conversion).

DistanceUnit into kilometers by writing an_object.distance.unit.destiny_unit[kilometers]. Notice that this is an association qualified by a derived attribute. Having the right Ratio, it is sufficient to divide the value of the original object by the divisor, which is an attribute of Ratio. The result value of this query is the quantity expressed in kilometers. Notice that this approach works with many kinds of magnitude, except for temperature, as the different scales of temperature do not make the zero mark coincident to the others, which is a precondition to use Ratio. In those cases, special classes could do the mathematics in the place of Ratio.

## 11.5 Measure

*Chapter 11 · p. 188*

An evolution of the Quantity pattern is the Measure pattern, which can be used when some different measures over an object must be taken possibly at different times. For example, a person in observation at a hospital may have many measures taken from time to time: body temperature, blood pressure, blood glucose level, etc. Thousands of different measures could be taken, but usually just a few are actually necessary for each patient. Therefore to avoid creating a concept with thousands of attributes with most of them likely being null, such as seen in Fig. 11–15, a better option is to use the Measure pattern as shown in Fig. 11–16.

Thus a patient may have a series of measures taken, each one assessing a different phenomenon and presenting a value that corresponds to a quantity (following the Quantity pattern).

It is still possible to make these patterns a little more sophisticated by adding attributes in the Measure class to indicate the instant of time at which the measure was taken and the validity of the measure. For example, the fact that a patient had a fever a couple of hours ago does not mean that she still has it. Instead of representing two attributes, one for time of measure and another for time of validity, we used the pattern Interval, that is explained later in this chapter. It means that any measure has an interval of validity that in this case is composed of two instants of Time, as the genericity class is referred here as Interval , Time.. See Fig. 11–17.

**Figure 11–15: A class with too many optional attributes referring to readings about a patient.** *(p. 188)*

> **Diagram content (transcribed from the figure image):** AVOID ("A single class have a great number of readings which are not mandatory"): Patient {+id; +name; «opt» +age: Natural; «opt» +blood_pressure, +temperature, +height, +weight, +hart_frequency, +glucose: Quantity; +an_so_on…}.

**Figure 11–16: An example of application of pattern Measure.** *(p. 189)*

> **Diagram content (transcribed from the figure image):** Measure pattern: Patient {+id: ID; +name: String} 1 — * Measure {+phenomena: TypeOfPhenomena; +value: Quantity}; «enumeration» KindOfPhenomena {age, blood_pressure, temperature, height, weight, hart_frequency, glucose}.

**Figure 11–17: A sophistication of pattern Measure with an interval of validity.** *(p. 189)*

> **Diagram content (transcribed from the figure image):** Measure with validity: Patient 1 — * Measure {+phenomena: TypeOfPhenomena; +value: Quantity; +validity: Interval<Time>}; same KindOfPhenomena enumeration.

**Figure 11–18: An evolution of Measure adding precision to its instances.** *(p. 189)*

> **Diagram content (transcribed from the figure image):** Measure with precision: Patient {+id; +name} 1 — * Measure {+phenomena: TypeOfPhenomena; +value: Quantity; +validity: Interval<Time>; +precision: Float}; «enumeration» KindOfPhenomena {age, blood_pressure, temperature, height, weight, hart_frequency, glucose}.

Another evolution for this pattern is to add an attribute to define the precision or accuracy of the measure taken. For example, body temperature usually is measured with a precision of 0.1 degrees (Celsius or Fahrenheit). Weight of a person is usually measured with a precision of a pound or kilo, and so on. A precision of 0.001 means that some measure has a precision of three decimal places. See Fig. 11–18.

## 11.6 Strategy

*Chapter 11 · p. 190*

It was mentioned that one of the great requirements challenges is to manage their change. Transitory requirements must especially be accommodated in the system design so that when they change, the impact to the system is minimized.

Some cases are relatively easy to address. For example, if it is already decided that the system must operate in different countries, the quantity pattern could be used to deal with currency and other measures that may vary from country to country as we already seen.

But there are much more complicated situations. For example, the tax calculation procedure may vary a lot from country to country and even from State to State in some countries. There are some taxes that are calculated in relation to the profit, others regarding the selling price, and so on. Methods for calculating taxes change from time to time, and in some countries new taxes are created every year. Systems must be prepared to cope with that, but the changes are completely unpredictable. Just configuring parameters usually is not enough.

Another example is a store’s discount policy. Current policy could be applying 10% off on orders above 100 dollars, for example. However, after some time, creative and unpredictable policies may be defined by the sales department, such as:

- Give a free book with a value up to 50 dollars for orders above 300 dollars.

- Give 20% off for up to two books on the customer’s birthday.

- Give 5% off on horror books on Friday the 13th.

- The customer spins a wheel, and it defines the discount she receives, from 1% to 10%.

Moreover, it would be possible to combine policies, if applicable, or choose the one that gives the higher discount.

The Strategy pattern suggests that in these cases, the procedure (e.g., calculate taxes or discount) must be separated from the data to which it applies. In other words, if a discount is applied to an order, then the discount should not merely be a method implemented in the Order class. The discount should be defined as something easier to change. The solution proposed by the Strategy pattern is to create an abstract class associated to the order. This abstract class may have concrete subclasses that represent concrete discount policies, as shown in Fig. 11–19.

Thus each instance of Order is associated to an instance of one of the subclasses of the Discount strategy. UML does not allow an attribute to be declared {abstract}; only classes and methods may be declared so. However, as derived attributes will be implemented by methods eventually, the idea of an abstract derived attribute stereotyped with «abstract» as shown in Fig. 11–19 is coherent to the UML spirit.

**Figure 11–19: Strategy pattern.** *(p. 191)*

> **Diagram content (transcribed from the figure image):** Strategy pattern: Order {«imm» «unique» +nr: Natural; «imm» +date: Date = Sismob.today(); +gross_total: Money; +/net_total: Money = gross_total-discount.amount} 1 — 0..1 Discount (abstract) {«abstract» +/amount: Money}; Order * — 1 buyer Person {«imm» «unique» +id: ID; +name; «imm» +birth_date: Date}; Discount subclasses PercentageDiscount {+percentage: Percentage; +lower_value: Money; +/amount}, BirthdayDiscount {+nr_books: Natural; +upper_value: Money; +/amount}, LinearDiscount {+percentage: Percentage; +/amount}.

Thus the abstract class Discount implements an abstract derived attribute amount, which is implemented in a concrete way in each of its subclasses. If some of the strategies need data from the customer or from the order to calculate the discount, that data can be accessed through the associations from the discount abstract class to the classes that own the information.

To complete the example of Fig. 11–19, the definition of the amount of each discount strategy is given below:

```ocl
Context PercentageDiscount::amount:Money
    def: gross = self.order.gross_total
    derive:
        if gross >= self.lower_value then
            self.percentage * gross
        else
            0
        endIf
```

In this case above, if the gross total of the order is higher than the lower value of the discount, a percentage of discount is applied to the gross total, otherwise zero discount is applied. Other strategy is:

```ocl
Context BirthdayDiscount::amount:Money
    def:
        birthday = self.order.buyer.birth_date
        today = System.today()
    derive:
        if birthday.day() = today.day()
        AND birthday.month() = today.month() then
            percentage * self.order.gross_total
        else
            0
        endIf
```

In this case above, if today is the birthday of the buyer, a linear discount defined by percentage is applied. Finally:

```ocl
Context LinearDiscount::amount:Money
    derive:
        percentage * self.order.gross_total
```

In this last case, a linear discount is applied to the gross total without any conditions. Remember that amount is the quantity of money that is subtracted from the gross_total in the Order for obtaining the net_total that is a derived attribute in the same class.

This pattern minimizes two problems related to requirements change. First, it keeps the discount strategy applied when the order was issued, even if strategies change in future. Second, if new strategies are created later, the team just must implement one or more subclasses for Discount. This usually does not affect the old strategies or the old orders.

## 11.7 Composite^2

*Chapter 11 · p. 192*

Different class instances may be grouped and treated as a single object recursively. The easier place to observe this pattern is by looking at drawing applications that allow independent geometric figures to be joined and treated as a new individual object. It can be seen in Fig. 11–20 where a geometric figure has five subclasses, line, triangle, square, polygon, and composed figure. On the other hand, a composed figure may be composed of any kind of geometric figure, lines, triangles, squares, polygons, and recursively composed figures.

> *Footnote 2:* Composite is the classic name for this pattern. However, if basic elements may be shared by different composite elements, it is the shared aggregation association that is used instead of the composite aggregation. This happens, for example, when strategies are composed.

**Figure 11–20: An example of recursively composed classes.** *(p. 193)*

> **Diagram content (transcribed from the figure image):** Composite pattern: abstract GeometricFigure with subclasses Line, Triangle, Square, Polygon, ComposedFigure; ComposedFigure 0..1 ◆— * GeometricFigure (a composed figure contains figures, including other composed figures).

**Figure 11–21: The composite pattern being applied to strategies.** *(p. 193)*

> **Diagram content (transcribed from the figure image):** Composite strategy: same Order/Person/Discount as Fig 11–19 plus CompoundDiscount {+/amount: Money} as a Discount subclass that aggregates 2..* Discounts (◇); subclasses PercentageDiscount, LinearDiscount, BirthdayDiscount, CompoundDiscount.

The same idea can be applied to the strategies seen in the last subsection. The combination of different discount strategies can be obtained, for example, by the sum of the values obtained for the derived attribute amount for each individual strategy, or by choosing the highest or lowest values among them. The choice of one or another combination produces different aggregated strategies.

Fig. 11–21 shows the definition of the SumDiscount strategy that can be a combination of two or more strategies. The amount attribute in SumDiscount is simply the sum of the value of the component strategies whichever they are.

At the same time, the expression below could be the definition of the derived attribute amount in class SumDiscount.

```ocl
Context SumDiscount::amount:Money
    derive:
        self.discount->sum(a_discount|a_discount.amount)
```

In the case of composing strategies, nothing prevents a strategy to belong to more than one compounded strategy. Thus the multiplicity on the origin of the composition association is “– | ,” meaning that the diamond must be white to indicate a shared aggregation.

## 11.8 Organizational hierarchy

*Chapter 11 · p. 194*

Another common situation consists of the need to represent organizational hierarchies. It is commonplace, for example, to represent the administrative organization of a company as a composition hierarchy as shown in Fig. 11–22.

However, hierarchies like this usually do not behave well. First, this kind of organization is not followed by every company: other companies may have different levels or different compositions among them. Second, the company structure may change over time. New divisions or offices may be created, some may be joined, and others split. Last, but not least, different views of an organization may exist at the same time; for example, the finance department may have a different view of the same organization.

How to deal with all that complexity in a conceptual model? By using the organizational hierarchy pattern.

The first approximation of a solution consists of not considering the different levels of an organization as concepts, but as instances of a single concept, as shown in Fig. 11–23.

In this way, flexibility is gained related to dealing simultaneously with organizational structures from different companies. Also, eventual changes in the organizational structure, such as adding more levels, or changing dependencies, may be easier to accomplish, because no code must be rewritten; only data accessible by the user must be changed.

**Figure 11–22: Straight representation of a company’s organizational structure by using classes for the different levels of composition.** *(p. 194)*

> **Diagram content (transcribed from the figure image):** Rigid organizational hierarchy: Company 1 ◆— * Division 1 ◆— * Office.

**Figure 11–23: A simple application of the organizational hierarchy pattern.** *(p. 194)*

> **Diagram content (transcribed from the figure image):** Organizational hierarchy pattern: OrganizationalStructure {+name: String; +type: OrganizationalStructureType} with reflexive composition 0..1 superstructure ◆— * substructure; «enumeration» OrganizationalStructureType {company, division, office}.

This pattern has some variations that may be used if concurrent hierarchies, superseding structures, or equivalent structures should also be represented.

The case for concurrent hierarchies involving some of the same structures may be solved with the use of a class which instances are the different views of the hierarchy. Let us suppose, for example, that some offices informally view themselves in groups, which are not a structure of the formal hierarchy. There are, then, two visions, the formal and the informal one, in which groups appear. In the formal hierarchy, offices are linked to divisions, but in the informal hierarchy, offices are linked to groups and groups are linked to divisions. Fig. 11–24 shows how to represent those parallel hierarchies.

Now, the View class may have two instances, one with name “formal” and other with name “informal.” The link between two organizational structures has an association class that associates the respective subordination to one of the views. Now, substructures may have different superstructures in different or in the same view. If it is the case that a substructure has only one superstructure in the same view, then an invariant could be applied:

```ocl
Context OrganizationalStructure
    inv:
        self.superstructure->forAll(:a_superstructure|
            self.superstructure->select(:b_superstructure|
                b_superstructure.subordination.view =
                a_superstructure.subordination.view)
            ->size = 1
        )
```

This invariant states that for each superstructure of an instance, the size of the set of superstructures with the same view as the original superstructure (a_superstructure) must be 1.

**Figure 11–24: Parallel hierarchies.** *(p. 195)*

> **Diagram content (transcribed from the figure image):** Hierarchy with views: OrganizationalStructure reflexive superstructure (0..1) / substructure (*), the link is an association class Subordination; Subordination * — 1..* View {+name: String}; OrganizationalStructureType {company, division, office, group}.

Looking at the model again, the team may perceive that it is very lousy regarding subordination relationships. In fact, any type of organizational structure can be sub or superstructure to any type of organization structure. Well, it could be verified by code, but it can also be represented in the conceptual model with an additional class Rule and a new invariant. The new class is shown in Fig. 11–25.

The model shows that instances of View may have a set of rules that establish that inside that view a structure of type A can only be a superstructure of type B if there is an instance of Rule with attributes sub valued with B and super valued with A. For example, in the official view of the organization discussed before, the existence of a rule with sub equals to office and super equals to division allows an office to be a substructure of a division. This is not enforced by the model as it is, however. To make it mandatory, an invariant must be created:

```ocl
Context Subordination
    inv:
        self.view->forAll(:a_view|
            a_view.rule(a_rule|
                self.substructure.type = a_rule.sub
                AND self.superstructure.type = a_rule.super
            )
        )
```

 )

This invariant states that for each subordination and each view associated to it, there exists a rule associated to the view with attributes sub and super corresponding respectively to the types of the substructure and superstructure of the subordination.

In the two last invariants, we introduce two new operations of OCL: forAll and exists. They behave in a very similar form that their equivalents in logic and mathematics: ’ and '.

**Figure 11–25: An evolution of the organizational structure pattern with subordination rules.** *(p. 196)*

> **Diagram content (transcribed from the figure image):** Same as 11–24 but superstructure multiplicity * and View 1..* — * Rule {+sub: OrganizationalStructureType; +super: OrganizationalStructureType} (rules state which type may be subordinated to which, per view).

## 11.9 Object joining

*Chapter 11 · p. 197*

One of the team’s assumptions that usually fails is that users will do everything right. That is not always the case. User failure (and sometimes sabotage) is still frequent, despite the efforts to build failsafe interfaces. A user could, for example, register a new person in the system and later discover that it was already registered. Entering an incorrect code or the impossibility of having a unique identification for a real-world object may cause this situation. The result is that two objects are registered in the system, both representing the same person, and each of them may possibly have its own set of treatments associated, some repeated, some not. In Brazil, the public health system must attend any person (citizen or not) that needs health care. Suppose someone that is unconscious and without identification. This person would be probably registered as John Doe with a special identification number and receive health care. If later the identity of this person is discovered, then the registry for this John Doe must be added to the registry of the identified person.

The solution when this kind of situation happens is to join the objects, usually copying one over the other. Thus the system may be prepared to do so.

Besides, it is not always an error that causes the need for a join. In some situations, there are objects considered equivalent by one group of people and not by another, and both situations must be represented simultaneously. In other cases, as in multiple view organizational hierarchies, it may be necessary to indicate that two structure elements in different views are equivalent, or that one succeeds another in time.

The following subsections present the main strategies to deal with these kinds of situations.

### 11.9.1 Copy and replace — 11.9 Object joining

The first strategy that comes to mind when it is necessary to join two objects consists of copying the data of one object over the second (copy and replace). The copy/replace command could be defined by a contract (see Chapter 12), and the team should define, for each attribute and each association, what must happen during the copy/replace command. Rules should be defined to decide if an attribute is going to be copied over the other, or if their values are to be added, or if the newest or highest of them must prevail, etc. Regarding the associations, the team must decide what happens: if one replaces the other, or if their properties are added, and so on.

The registry of the date of the last inclusion or change of a concept may be useful for deciding which attribute must be kept in the case of a conflict. For example, if a registered customer makes a new record, and it is going to be resolved, then the most recent address must be kept, not the oldest one. On the other hand, all her orders must be added to the resulting instance.

After performing the copy/replace command, the instance that was copied must be destroyed, and any references to it must be redirected to the instance that received the data.

To avoid losing data by thinking that two registers are the same and after merging them discovering that that was not the case, it would be useful to use one of the temporal patterns in the class that may be merged. Temporal patterns are described in the end of this chapter, and they would allow to recover the original objects after merging.

### 11.9.2 Superseding — 11.9 Object joining

Superseding is a technique that can be used when the original object must be kept and not destroyed. Superseding is applicable, for example, in the case of organizational structures that are succeeded in time. Suppose that the departments of marketing and sales are joined into a single department of customer contact; the original departments must be marked as no longer active, and a new department must be added as their successor. The superseding strategy may be implemented by a reflexive association, being an evolution of the organizational hierarchy pattern in this case, as shown in Fig. 11–26.

The derived attribute active indicates if the structure is active or if it has been superseded. It is true if the set of superseders is empty and false otherwise.

To maintain the original organizational structure even if it is not active anymore may be important for registry purposes. Someday someone may need to know how much a given department that does not exist anymore spent on toothpicks.

It would be useful to add an association class to the superseded/superseder association; its attributes could indicate, for example, the date when the superseding event taken place, or the context or view in which it must be considered. This can be seen in Fig. 11–27.

In this case, when an organization is divided into two, for example, there will be two links between the superseded organization and the superseder organizations, and two superseding events may be linked to both links.

If there is a need to account for the multiple superseding links that belong to the same event, a specification class for SuperSeding can be added for grouping the links that were created by the same event, as seen in Fig. 11–28.

To deal with this kind of situation, the team should also consider applying one of the temporal patterns seen in the end of the chapter.

### 11.9.3 Essence/appearance — 11.9 Object joining

Another situation that can still often happen is the existence of objects that are considered equivalent but must be kept as separated objects. This is not a registry error, and it is not an object that supersedes another: this is object equivalence.

**Figure 11–26: An example of superseding strategy.** *(p. 198)*

> **Diagram content (transcribed from the figure image):** Hierarchy with history: OrganizationalStructure {+name; +type; +/active: Boolean = self.superseder->isEmpty()} with reflexive superstructure 0..1 ◆— * substructure and reflexive superseded * — * superseder association.

**Figure 11–27: Evolution of the supersede pattern.** *(p. 199)*

> **Diagram content (transcribed from the figure image):** Same as 11–26 with association class SupersedingEvent {+date: Date; +reason: String} on the superseded/superseder association.

**Figure 11–28: Superseding links grouped by a single superseding event specification.** *(p. 199)*

> **Diagram content (transcribed from the figure image):** Same with association class SupersedingLinking * — 1 specification SupersedingEvent {+date: Date; +reason: String} (one event can supersede many structures at once).

Object equivalence may be modeled using an essence object that is associated to a set of equivalent objects. As opposed to copy/replace, the original objects are kept, and as opposed to superseding, there is no active or superseded object: all associated objects are equivalent. Fig. 11–29 shows an example of a class (Book) that accepts that its members share a common essence.

In the example, we consider that the same book in essence, especially a classic work, may be published by different publishers. Each publication is distinct, with a different ISBN and number of pages. Even the title and author’s name may vary (proper names may be translated or abbreviated sometimes). But the essence of the text is the same. Some users may be interested in ordering Plato’s The Republic from a specific publisher, and others may be interested in the book independently of the edition or publisher. Thus the users interested in a specific publication are looking for the appearance (a given instance of Book), and the users interested in the text are looking for the book in essence—the publisher does not matter. The second group of users, when viewing any edition of The Republic, must also be allowed to view other instances of Book linked to the same EssenceBook if they exist. In other words, if you look for book a_book and if a_book.essence_book- . notEmpty(), then you will see a_book.essence_book.book, which is a set of books with the same essence.

**Figure 11–29: An example of application of pattern Essence/Appearance.** *(p. 200)*

> **Diagram content (transcribed from the figure image):** Object joining (essence): Publisher {«imm» «unique» +id: IDPublisher; +name: String} 1 — * Book {«imm» «unique» +isbn: ISBN; «imm» +title; «imm» +author; «imm» +pageCount: Natural}; Book 2..* — 0..1 EssenceBook (groups books that are the same work).

Not every Book must be linked to an EssenceBook, only those that participate in an equivalence class. Also, there must be at least two equivalent books to create an EssenceBook. This is why the association role from EssenceBook to Book is marked with 2.– .

Objects are considered equivalent if they are linked to the same essence object. The essence object exists only to establish that equivalence; usually it will not have any other properties. Otherwise, maybe the specification class pattern could be used instead.

### 11.9.4 Undoing a join — 11.9 Object joining

Just when the team thinks that the real world cannot be more complex, it becomes so. Therefore if there is a possibility of joining objects, it is also possible that joined objects must be separated again. Once again, these commands may be performed through well-planned operations available at the system’s user interface.

To allow the joins of the copy/replace technique to be undone, a backup of the original objects must be kept, because the technique destroys one of the objects and disfigures the other. A log on the operations done over the object after the merge must also be kept and possibly redone in one of the original objects after splitting.

The superseding technique allows the join to be undone too. Despite there are other ways to do that, maybe the best one is to perform the merging or splitting operations in reverse order. For example, if the departments of marketing and sales are merged into a department of customer care, undoing this operation would be just to split the department of customer care into a new department of marketing and a new department of sales.

In the case of essence/appearance, it is necessary to remove the association (and the essence object if less than two links to it remain).

However, in every case it is important to decide how to deal with eventual changes within the object that occurred while it was joined with the others. Again, temporal patterns may help doing things in these cases.

## 11.10 Account/transaction

*Chapter 11 · p. 201*

The account/transaction pattern is closely related to business, but it has wide applicability. Products in a store may be cataloged, ordered, received, delivered, discarded, etc. Such movements, as well as the financial transactions involved with them, give origin to concepts such as Order, Delivery, Discard, Return, Payment, and Receiving, each one with its own attributes and associations.

However, it is possible to identify a common core for all these concepts and many more, which is constituted by a single and powerful pattern.

An Account is a concept that bears quantities of something (such as products or money). An Account has a balance that usually consists of the sum of every deposit or withdrawal.

On the other hand, deposits and withdrawals are usually just transactions of goods or money from an account to another. Thus a Transaction consists of two movements: a deposit in one account and a withdrawal of the same value from another account. Fig. 11–30 illustrates those classes.

A consistent transaction with two entries such as the one in Fig. 11–30 needs two entries with the same absolute value but opposite signs. In other words, if a transaction takes 5 dollars from an account, it must necessarily deposit 5 dollars into another account; the withdrawal has a negative sign and the deposit a positive sign. Thus the Transaction class needs the following invariant:

```ocl
Context Transaction
    inv:
        self.movement->sum(:a_movement|a_movement.value)=0
```

This means that for each instance of Transaction, the sum of the value of the two associated movements must be zero.

The derived attribute balance of class Account is defined as the sum of every movement linked to that specific Account:

```ocl
Context Account::balance
    derive:
        movement->sum(value)
```

Many situations related to the store example could be modeled from a set of instances of class Account, such as:

- For each supplier, there is an instance of Account from which products are “withdrawn,” that is, it is an entry account, and its balance becomes more negative as products are ordered from the supplier.

**Figure 11–30: Classes for the Account/Transaction pattern.** *(p. 201)*

> **Diagram content (transcribed from the figure image):** Account/transaction pattern: Account {«unique» +name: String; +/balance: Integer = entry->sum(value)} 1 — * Movement {+value: Integer} 2 — 1 Transaction {movement->sum(value) = 0} {«imm» +name: String}.

- There is an account for orders expected, which contains the products that were ordered from the supplier but that had not yet arrived.

- There is an account for stock containing the available products.

- There is an account for sold products containing products sold but not yet delivered.

- There is an account for delivered products containing products delivered but not yet confirmed by the customer.

- There is an account for confirmed delivery containing products delivered and confirmed by the customer. Its balance represents the whole set of products that the customer has bought from the store.

In parallel to product transactions, there are concomitant money transactions. There are receivable accounts, payable accounts, received accounts, paid accounts, investment, debts, values saved for paying taxes, etc.

Thus many transactions of the bookstore example could be modeled as an instance of Transaction. For example:

- An order is a transaction that takes products from a supplier entry account and deposits them into an expected orders account.

- The arrival of the products is a transaction that takes from the expected orders account and adds to the stock account.

- A sale is a transaction that takes from the stock account and adds to the sold products account.

- A delivery is a transaction that takes from the sold products account and adds to the delivered products account.

- A return is a transaction that takes from the delivered products account and adds to the stock account (if the products are in good shape).

- A confirmation of delivery is a transaction that takes from the delivery account and adds to the confirmed delivery exit account.

As an example, imagine a company that just started, where five instances^3 of the Account class were created: supplier, pending orders, stock, sold, and delivered. Fig. 11–31 shows the initial state for those objects when all accounts have a zero balance.

Fig. 11–32 shows the resulting set of objects when a purchase order (instance of Transaction) is created. The order was issued for 50 products. Account supplier balance is now 250, and account pending orders is 150.

Fig. 11–33 shows the state of the accounts if only 40 of the 50 ordered books arrive. In this case, 10 products are still pending and 40 are in stock. Still 250 are in the balance of the supplier.

Fig. 11–34 shows the state of the accounts after 25 products are sold. In this case, supplier keeps 250, pending orders are 10, stock is updated to 15, and sold to 25.

And finally, Fig. 11–35 shows how the accounts look like after the 25 books sold are delivered. Account sold is updated to 0 and delivered to 25.

3 The example deals with only five instances for simplification. Many others could be included.

**Figure 11–31: Initial state of an accounting system for products.** *(p. 203)*

> **Diagram content (transcribed from the figure image):** Same account/transaction model plus INSTANCES: five :Account objects named "supplier", "pending orders", "stock", "sold", "delivered", each with balance = 0.

**Figure 11–32: State of the accounts after a purchase order of 50 products is issued.** *(p. 203)*

> **Diagram content (transcribed from the figure image):** Account/transaction instances after transaction "purchasing": movements −50 on "supplier" and +50 on "pending orders" (balances supplier −50, pending orders 50, stock/sold/delivered 0).

**Figure 11–33: State of the accounts after 40 products arrive at the stock.** *(p. 204)*

> **Diagram content (transcribed from the figure image):** After a second transaction "arrival": movements −40 on "pending orders" and +40 on "stock" (balances supplier −50, pending orders 10, stock 40, sold 0, delivered 0).

**Figure 11–34: State of the accounts after 25 products are sold.** *(p. 204)*

> **Diagram content (transcribed from the figure image):** After a third transaction "sale": movements −25 on "stock" and +25 on "sold" (balances supplier −50, pending orders 10, stock 15, sold 25, delivered 0).

**Figure 11–35: State of the accounts after the delivery of 25 products.** *(p. 205)*

> **Diagram content (transcribed from the figure image):** After a fourth transaction "delivery": movements −25 on "sold" and +25 on "delivered" (balances supplier −50, pending orders 10, stock 15, sold 0, delivered 25). Each transaction's movements sum to zero.

New transactions and accounts may be created dynamically (i.e., without having to recompile the system). For example, a new transaction may be created for returning products, which moves products from the delivered account back to the stock account. Also, a new transaction for discarding products could be created moving products from the stock or sold accounts to a new account for discarded products. Parallel financial transactions could be created as well by using Account and Transaction.

### 11.10.1 Multilegged transactions — 11.10 Account/transaction

This pattern is very interesting as an example of how a simple powerful idea can deal with so many different situations. It has many variations and sophistications. For example, multilegged transactions may be created, if necessary, for moving from more than one account to a single account, or from a single account to more than one account, or even from more than one account to more than one account at the same time. To accomplish this variation, the multiplicity role from Transaction to Movement should be changed from 2 to 2.– . .

### 11.10.2 Memo movements and memo accounts — 11.10 Account/transaction

Another important variation is the use of memo movements. For example, when money is received, taxes must be paid, but not necessarily immediately. Thus when a transaction moves money from a customer account to the store balance account, a quantity of money equivalent to the taxes due could be registered into a tax memo account. When it is time to pay taxes, the balance of the memo account registers the amount to be paid.

Memo accounts and normal accounts share the same attributes but not the same associations. Thus they are defined as subclasses of an abstract class Account. The same happens with memo movements and normal movements. Fig. 11–36 shows the model.

Memo and normal movements are not distinguished except for the kind of Account subclass they are linked and to the fact that a Transaction still must have only 2 normal movements, or 2.– * if multilegged transactions are allowed. At the same time, a Transaction can have any number of memo movements, and those memo movements are not used in the invariant in class Transaction. Only normal movements should sum zero in a Transaction. Fig. 11–37 shows the initial state of an example where a sale transaction can be registered with money being moved between normal accounts and a tax of 15% being registered in a memo account.

What happens next is a sale when 400 Mira is transferred from the client account to the target organization account and a tax of 15% is registered in the tax due memo account. The resulting situation is depicted in Fig. 11–38.

Notice that at this point, the taxes are not being paid. Money is transferred between the two normal account and sum zero, and the 15% of taxes due is simply registered in a memo account for future providences.

Finally, let us see what happens when the day to pay taxes arrives. Then the balance registered in the taxes due must be transferred from the organization’s account to the government account, and the memo account should be reset to zero. This is shown in Fig. 11–39.

And this completes our example.

**Figure 11–36: Memo and normal accounts and memo and normal movements.** *(p. 206)*

> **Diagram content (transcribed from the figure image):** Account/transaction with memo accounts: abstract Account {«unique» +name: String; +/balance: Integer = normal_movement->sum(value)} with subclasses NormalAccount and MemoAccount; abstract Movement {+value: Integer} with subclasses NormalMovement and MemoMovement; NormalAccount 1 — * NormalMovement; MemoAccount 1 — * MemoMovement; Transaction {normal_movement->sum(value) = 0} {«imm» +name: String} 1 — 2..* NormalMovement and 1 — * MemoMovement.

**Figure 11–37: Initial state of a transaction with a memo account.** *(p. 207)*

> **Diagram content (transcribed from the figure image):** Instances before: NormalAccount "our account" M$0.00; NormalAccount "client account" M$1000.00; NormalAccount "taxes paid" M$0.00; MemoAccount "taxes due" M$0.00.

**Figure 11–38: The status of the objects after a sale is registered.** *(p. 207)*

> **Diagram content (transcribed from the figure image):** After Transaction "sale": NormalMovement +M$400.00 to "our account" (balance M$400.00), NormalMovement −M$400.00 to "client account" (balance M$600.00), MemoMovement M$60.00 to MemoAccount "taxes due" (balance M$60.00); "taxes paid" stays M$0.00 (memo movements need not balance).

**Figure 11–39: The status of the objects after taxes are paid.** *(p. 208)*

> **Diagram content (transcribed from the figure image):** After a second Transaction "tax payment": NormalMovement −M$60.00 on "our account" (balance M$340.00), NormalMovement +M$60.00 on "taxes paid" (balance M$60.00), MemoMovement −M$60.00 on MemoAccount "taxes due" (balance M$0.00); "client account" stays M$600.00. Transaction "sale" keeps its movements (+400, −400, memo +60).

## 11.11 Range or interval

*Chapter 11 · p. 208*

When an object has a pair of attributes indicating the beginning and end of some phenomena, such as initial and final date, instead of representing it as two separated attributes, it is advisable to declare a single attribute type such as Interval (or Range), as shown in Fig. 11–40.

The primitive Interval is parameterized, meaning that when an instance is created, it must indicate the Type to be used to define its attributes. For example, an interval over Date could be referred to as Interval , Date., and an interval over a quantity defined as Distance could be referred to as Interval , Distance.. See Fig. 11–41 for an example of use of this pattern.

There are at least two reasons for using an interval instead of two attributes:

- If the lower and upper bounds are separated attributes in a conceptual class, they would have a strong relation between them. This violates the high cohesion principle explained in Section 11.2.

- Operations that are specific to intervals (e.g., checking if a value is inside an interval) will be needed. If there is a specific Interval primitive type, these operations may be

**Figure 11–40: A primitive type Interval with genericity.** *(p. 209)*

> **Diagram content (transcribed from the figure image):** «primitive» Interval<Type> {«opt» +lower_bound: Type; «opt» +upper_bound: Type} — range/interval pattern.

**Figure 11–41: An example of use of pattern Interval.** *(p. 209)*

> **Diagram content (transcribed from the figure image):** Freeway {+id: FreewayID; +name: String; +period_of_construction: Interval<Date>; +lane_width: Interval<Size>; +max_speed: Interval<Speed>} — attributes typed as intervals.

**Figure 11–42: Interval with open and close options for bounds.** *(p. 209)*

> **Diagram content (transcribed from the figure image):** Interval<Type> with open/closed bounds: {«opt» +lower_bound: Type; «opt» +upper_bound: Type; +lower_bound_open: Boolean; +upper_bound_open: Boolean}.

implemented once just in the primitive. If two attributes are used instead, each class where they are declared should implement its own version of the operations on intervals.

It is much more reasonable to implement operations just once in a high-cohesion class, than implementing them many times in low-cohesion classes.

As seen in Fig. 11–41, both attributes of the Interval class are optional, which means that intervals may be undefined in one or both ends. For example, an interval that starts at January 1, 2023 and has no upper bound could be defined with lowerBound 5 “01/01/2023” and upperBound 5 null.

Evolutions of this pattern could consider the mathematical properties of intervals. For example, there are open and closed intervals: [0.10] is a closed interval that includes 0 and 10, while (0.10) is an open interval that excludes 0 and 10. Furthermore, (0.10] excludes 0 and includes 10 and [0.10) includes 0 and excludes 10. This evolution could be implemented simply by adding two Boolean attributes to the class Interval: lower_bound_open and upper_bound_open as seen in Fig. 11–42.

Finally, to enforce the definition that an interval must have a lower_bound smaller than its upper_bound, if they exist, an invariant can be added to the Interval class:

```ocl
Context Interval
    inv:
        self.lower_bound->notNull AND selfu_pper_bound->notNull
        IMPLIES self.lower_bound <= self_upper_bound
```

Context Interval inv: self.lower_bound->notNull AND self_upper_bound->notNull IMPLIES self.lower_bound <= self_upper_bound

Here we considered that an interval with the same lower and upper bounds is valid, such as [10..10]. Also, the invariant above uses the operator IMPLIES of OCL. This is a predicate equivalent to the implication operator in propositional logic, and X IMPLIES Y is false if and only if X is true and Y is false.

## 11.12 Temporal patterns

*Chapter 11 · p. 210*

Frequently, the analyst faces the need to deal with time. For example, it may be necessary to represent the relations between people and their jobs. But, if the association between people and jobs represents only the present time, then the information of former jobs will be lost when someone quits the job. This section discusses some patterns that deal with that important notion.^4

### 11.12.1 Effectivity — 11.12 Temporal patterns

When an object is valid for some time. For example, when the temperature of a patient is measured, it is considered valid for a certain period. In an extreme example, a temperature measure taken today will not be considered valid after 7 days. Other measures may have longer periods of validity. For example, if an adult measure 6 feet, this measure may be considered valid for years.

The period between the act of taking a measure and the end of its validity is the effectivity of the measure, and in is the name of the first temporal pattern.

Effectivity may be represented as an interval attribute in a class that represents the object that has validity time, as seen in Fig. 11–43.

It can also be applied to products, such as medicine, renting contracts.

**Figure 11–43: Temporal pattern Effectivity.** *(p. 210)*

> **Diagram content (transcribed from the figure image):** Measure {+phenomena: KindOfPhenomena; +value: Quantity; +effective: Interval<Time>}.

> *Footnote 4:* Martin Fowler presents a nice summary on many temporal patterns at http://martinfowler.com/eaaDev/ timeNarrative.html. Consulted in: May 31, 2023.

### 11.12.2 History — 11.12 Temporal patterns

If historical information must be stored about the past states of an association, attribute, or even a whole object, then the History pattern may be used. In the example of Fig. 11–44, the stereotype «history» is used to indicate that a person may have only one job at an instant, but her former jobs are remembered by the association.

Notice that the stereotype is applied to the whole association and not only to a role. This means that if the association is navigable in two ways, both roles maintain history: the person remembers the organizations she worked before and the organization remember persons that worked for it, but that are not employed anymore.

The stereotype of the association of Fig. 11–44 means that a person must have just zero or one job currently, but she may have had other jobs in the past. These past jobs may be recovered as items in a list. In other words, it is possible to recover the last job, the job before the last, and so on.

When it comes to design, each class with an association with a navigable role implements a method for accessing the elements linked. In the example of Fig. 11–44, the design class for Person would have a getter query get_job() that returns the organization where this person is working or the empty set if this person is unemployed. If the association is stereotyped with «history», in addition to that standard method get_job(), there would exist another method with a parameter, get_job(index:Natural), where get_job(0) returns the current job and is the same as get_job(). However, get_job(1) returns the last job before the current one. Also, get_job(2) returns the job before the job before the current one, and so on. If there is no job for the index given, then the query returns the empty set.

In practice, this pattern can be implemented by two associations, as shown in Fig. 11–45: one representing the current job, if any, and the other representing a sequence (yes, a sequence because one can work in the same organization more than once) of jobs. The stereotype is, then, a way to abbreviate a more complex structure, replacing it with a simpler one.

**Figure 11–44: History patters applied to an association.** *(p. 211)*

> **Diagram content (transcribed from the figure image):** Temporal association with stereotype: Person {«imm» «unique» +id: ID; +name} * —«history»— 0..1 job Organization {«imm» «unique» +id: IdOrganization; +name} (keeps the history of jobs).

**Figure 11–45: A possible implementation for the History pattern for an association.** *(p. 211)*

> **Diagram content (transcribed from the figure image):** History made explicit: Person * employees — 0..1 current_job Organization, plus Person * {sequence} former_employees — * {sequence} former_jobs Organization.

**Figure 11–46: An example of attributes with History pattern.** *(p. 212)*

> **Diagram content (transcribed from the figure image):** «history» on attributes: Person {«imm» «unique» +id: ID; «history» +name: String; «history» +address: String}.

**Figure 11–47: A possible implementation of attributes with history using superseding.** *(p. 212)*

> **Diagram content (transcribed from the figure image):** Versioning: Person {«imm» «unique» +id; «imm» +name; «imm» +address} with reflexive 0..1 newer_version / 0..1 older_version association.

**Figure 11–48: A whole class stereotyped with «history».** *(p. 212)*

> **Diagram content (transcribed from the figure image):** Class-level «history» Person {«imm» «unique» +id: ID; +name: String; +address: String} (all changes of the object are kept).

This pattern can also be applied to attributes. If a person changes name and address and we should maintain this information for any reason, then the pattern can be used, as in Fig. 11–46.

On interesting way to implement this pattern in attributes is by using the superseding pattern, such as shown in Fig. 11–47. Here name and address become immutable. They cannot be changed, but a new version of the object with other values may be created and supersedes the current one. This is the same technique used by configuration management systems. This implementation already works for all attributes of the class that are not immutable and can be used as well when the whole class is stereotyped with this pattern as seen in Fig. 11–48.

### 11.12.3 Temporal — 11.12 Temporal patterns

The History pattern is not capable of answering what was the value of an attribute or association role at a given moment of time. To represent that kind of information, an evolution of that pattern may be used: an association that in addition to sequential memory has time memory, as shown in Fig. 11–49.

**Figure 11–49: Temporal pattern applied to an association.** *(p. 213)*

> **Diagram content (transcribed from the figure image):** «temporal» association: Person * — «temporal» — 0..1 job Organization (each link has a validity period).

**Figure 11–50: A possible implementation for the Temporal pattern.** *(p. 213)*

> **Diagram content (transcribed from the figure image):** Temporal association made explicit: Person 1 — {sequence} * Job {+period_of_contract: Interval<Date>} * — 1 Organization.

A temporal association or attribute has at least three methods to consult its value. In the case of the example, where the job role association is temporal, the following methods would exist:

- getJob(): Returns the current job of a person or the empty set if the person is currently unemployed.

- getJob(index:Natural): Returns the current or former job of a person depending on the index argument, or the empty set if there is no job at that index. For example, getJob (0) returns the current job, if any, getJob(1) returns the job before the current one, if any, and so on.

- getJob(date:Date): Returns the job a person had at the end of a given date or the empty set if the person was unemployed at that date.

If it was required to know the job of a person at a given time of the day, then the primitive type Date can be replaced by Time, which refers to year, month, day, hour, minute, and second. For applications that demand more precision, milliseconds, microseconds, and so on could be used additionally.

Fig. 11–50 presents a possible implementation the «temporal» stereotype.

The Job class does not have a pair of attributes such as initial_date and end_date, but a single attribute period_of_contract with type Interval , Date., representing an interval between hiring and firing.

In the case of attributes or classes that need to know their values in given dates in the past, as shown in Fig. 11–51, the implementation can also follow the superseding pattern as shown in Fig. 11–52. But, in this case, a stamp of time is added to the supersede association.

**Figure 11–51: A class with temporal attributes.** *(p. 214)*

> **Diagram content (transcribed from the figure image):** Person {«imm» «unique» +id: ID; «temporal» +name: String; «imm» +birth_date: Date} — a temporal attribute.

**Figure 11–52: A possible implementation of the temporal pattern for attributes and objects.** *(p. 214)*

> **Diagram content (transcribed from the figure image):** Temporal attribute implemented by versions: Person {«imm» «unique» +id; «imm» +name; «imm» +birth_date} with reflexive 0..1 newer_version / 0..1 older_version association and association class Update {«imm» +time: Time}.

For example, some countries allow people to change their names after marriage, divorce, or decision of a judge. In Fig. 11–51, the ID and birthdate of a person are not supposed to change. However, the different names of that person may be remembered by the system, and the time each change happened too.

### 11.12.4 Bitemporal — 11.12 Temporal patterns

Not only in science fiction but also in many current information system applications, time may be considered two-dimensional. There is a dimension of time in which events occur and another dimension where we acknowledge that an event occurred.

This is a new pattern known as Bitemporal, because it has two dimensions for time: the time when an event happened and the time we were informed that the same event happened. Those times not always are coincident. For example, it is said that when Lincoln was murdered, the news took 15 days to reach Europe. Fig. 11–53 shows a situation where a bitemporal pattern is applied to an association.

Looking at this model, imagine that the association says that a Person named Mary is currently working for Organization X. However, today we discovered that in fact Mary is not working at that organization for the last three months. There are two dates to be recorded here: the date Mary changed jobs and the day our information system received that information.

This knowledge may justify eventual actions done during the time when our system was not updated. If only the date of change is recorded, than it would be impossible to know that this information was not available for a certain time.

Sometimes, especially for accountability or legal procedures, knowing when a record was changed is crucial. The bitemporal pattern is an elegant way to keep track not only of the line of events but also the line of our knowledge about events.

Now a new getter may be introduced for the role job: getJob(change_date, knowledge_date:Date). The first argument is the instant of time we are interested in, and the second argument is the instant of time of our knowledge about it. For example, if we want to answer the question “On June 15, 2023, where did we believe that Mary worked on June 1, 2023?” we could use the query get_job(“06/01/2023,” “06/15/2023”).

**Figure 11–53: Bitemporal pattern.** *(p. 215)*

> **Diagram content (transcribed from the figure image):** «bitemporal» association: Person * —«bitemporal»— 0..1 job Organization (both real-world validity and system-knowledge time recorded).

**Figure 11–54: A possible implementation for pattern bitemporal.** *(p. 215)*

> **Diagram content (transcribed from the figure image):** Bitemporal made explicit: Person 1 — * {sequence} Job {+hapening: Interval<Date>; +knowing: Interval<Date>} * {sequence} — 1 Organization.

If we want to know where Mary worked on June 1, 2023, based on our current knowledge, we could use the getter mentioned for the temporal pattern: get_job(“06/01/2023”), which is short for get_job(“06/01/2023,” today).

Fig. 11–54 presents a possible implementation for that stereotype.

Now there are two date ranges in the class Job, one for registering the time the job was effective (happening) and the other to represent the range of time when this information was considered true (knowing).

Each time our knowledge about the job of a person is changed, a new instance of Job is created. The happening attribute establishes when the job was effective, and the knowing attribute establishes the point from when we believed that. The upper bound of the two intervals in Job would usually be kept undefined while it represents our current knowledge, that is, while that information was not overridden by newer (eventually contradictory) information.

The bitemporal pattern can also be applied to attributes or entire classes, just like the temporal pattern and again using the supersede pattern.

## 11.13 Discussion

*Chapter 11 · p. 215*

A good conceptual model produces an organized structure that is suitable to generate an already normalized database. It incorporates structural rules that prevent information from being represented in an inconsistent way; it also simplifies the code that will be generated because it minimizes and organizes consistency checks, and several verifications that are guaranteed by the model itself do not need to be performed by the code.

The use of suitable design patterns in situations where they are necessary simplifies the conceptual model and gives it more flexibility and quality. It is, therefore, a powerful tool for agile modeling. Many other patterns exist, and teams may create their own new patterns. It just should be kept in mind that the creation of a pattern is justified only when its benefits pay for the effort expended in creating and remembering it.

## Questions (Chapter 11)

1. In Fig. 11–30, there is no explicit invariant that states that a Transaction cannot be linked to movements that are linked to the same account, because the structure of the model already demands is. Why is it not necessary?

2. Apply the Account/Transaction pattern to the parallel financial transactions of the example shown in Figs. 11–31 to 11–35. As the bills may be paid forward, it may be necessary to use memo entries. Define the set of instances of Account and Transaction that are necessary and describe them.

3. Use Google or another search mechanism to find examples of conceptual models including classes with attributes. Analyze those classes and check if they present cohesion problems. Propose alternative solutions to them if necessary.

4. A system for registering genealogical trees allows different users to check if they have coincident people in their own trees. If this is the case, the shared person is marked in each tree as equivalent to the other. Thus two cousins, for example, who have the same grandfather, may have a coincident registry in their trees. Which of the three strategies of object joining is best for dealing with this case? Why? Elaborate a model for representing people in the genealogical trees using that pattern.

5. Look at Fig. 11–19 and create a new discount strategy that gives a percentage of discount for sales with more than a certain number of products.

