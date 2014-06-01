Dynamic typing vs. Static typing
--------------------------------

### G. Steel (referenced by M. Furr, B. Cannon)

>A dynamic language is one that defers as many decisions as possible to
runtime.
    

### M. Furr - Static Type Inference in Ruby:

>Dynamic typing is appealing because it ensures that no correct program exe-
cution is stopped prematurely—only programs about to “go wrong” at run time
are rejected.

>Moreover, with pure dynamic typing, programmers lose the con-
cise, automatically-checked documentation provided by type anno-
tations.

### F. Ortin - Union and intersection types to support both dynamic and static typing

>Static typing is an unquestionably important tool for software development,
offering the programmer advantages such as early type error detection,
better documentation and abstraction, and more opportunities for compiler
optimizations. Nevertheless, dynamically typed languages provide great
flexibility at runtime, making them ideally suited for prototyping
systems with changing or unknown requirements, or which interact with other
systems that change unpredictably (data and application integration)

###S. Tu - MINO: Data-driven approximate type inference for Python

>Dynamic programming languages, such as Python and Ruby, are
becoming the languages of choice for many developers. The lack
of strict compile-time type checking is often cited as making de-
velopment cycles faster. However, a big drawback to dynamically
typed languages is that it is impossible to know the exact type of
a given variable at compile time; it is a well known result that this
problem is undecidable for such languages

### J. Aycock - Aggressive Type Inference
    
> Python is a "dynamically typed" language because, in general, 
the type of any variable is not known definitively until run-time.
    
> Giviving people a dynamically-typed language does not mean that they 
write dynamically typed programs.

### E. Maya - A Static Type Inference for Python

> Dynamic languages, like Python, are attractive because they
guarantee that no correct program is rejected prematurely.
However, this comes at a price of losing early error detection,
and making both code optimization and certification harder
tasks when compared with static typed languages. 

> However, when time performance is not absolutely critical, the speed and
simplicity of the development cycle and the safety and clarity of the
code justify the use of high-level languages, such as Python.

> Python is dynamically typed and allows variables to take values of different
types in different program places. 

### S. Hanov - Type inference using the Cartesian Product Algorithm on a
dynamically typed language
   
> ... duck-typed languages--languages for which the variables are bound to
types when they are assigned a value. In these languages, it is not even
obvious to the programmer if calling a method will work, and any extra
information that can be gleaned by the compiler would be helpful.

### A. Holkner - Evaluating the dynamic behaviour of Python applications
    
> The Python programming language is typical among dynamic languages in that
programs written in it are not susceptible to static analysis. This makes
efficient static program compilation difficult, as well as limiting the
amount of early error detection that can be performed.

Duck typing
-----------

### F. Ortin - Union and intersection types to support both dynamic and static typing

> Duck typing is a property offered by most dynamically typed
languages that means that an object is interchangeable with any other
object that implements the same dynamic interface, regardless of whether
those objects have a related inheritance hierarchy or not.


### S. Hanov - Type inference using the Cartesian Product Algorithm on a dynamically typed language

> Dynamically typed, (or “duck typed”) languages are useful for
rapid prototyping and code reuse. In languages that have duck
typing, a variable’s value determines what it can do, and implies
that an object is interchangeable with any other object that
implements the same interface, regardless of whether the objects
are related by inheritance.


Type inference
--------------

### M. Salib - Faster than C: static type inference with Starkiller

> From a type inference perspective, Python is a large and complex language.
In contrast to other languages that rely heavily on type inference for
performance, such as Eiffel, Haskell, or the many variants of ML, Python
was designed with little thought as to how the language semantics would
hinder or help type inference. Instead, Python’s semantics evolved over
several years in response to feedback from a community of skilled
practitioners. Thus, while languages like Haskell suffer occasional design
flaws that had to be imposed specifically to make type inference easier,
Python makes no such compromises in its design, which only makes
Starkiller’s job that much harder. One example of type inference dictating
language development is how Haskell forbids the polymorphic use of
functions passed as arguments because the Hindley-Milner type inference
algorithm that Haskell relies upon cannot handle such nonlocal usage. This
limitation stems directly from Hindley-Milner’s focus on incremental
inference rather than whole program analysis.

Type systems
------------

### B. Pierce - Types and programming languages

> A *type system* is a tractable syntactic method for proving the absence of
certain program behaviors by classifying phrases according to the kinds of
values they compute.

> A *type system* can be regarded as calculating a kind of static approximation
to the run-time behaviors of the terms in a program.

> The word “static” is sometimes added explicitly — we speak of a “statically
typed programming language,” for example — to distinguish the sorts of
compile-time analyses we are considering here from the dynamic or latent
typing found in languages such as Scheme, where run-time type tags are used
to distinguish different kinds of structures in the heap. *Terms like “dy-
namically typed” are arguably misnomers and should probably be replaced by
“dynamically checked,” but the usage is standard*.

> Being static, type systems are necessarily also *conservative*: they can 
categorically prove the absence of some bad program behaviors, but they cannot
prove their presence, and hence they must also sometimes reject programs
that actually behave well at run time. 
...
The tension between conservativity and expressiveness is a fundamental fact
of life in the design of type systems. The desire to allow more programs to
be typed—by assigning more accurate types to their parts—is the main force
driving research in the field.

> Retrofitting a type system onto a language not designed with typechecking
in mind can be tricky; ideally, language design should go hand-in-hand with
type system design.  *One reason for this is that languages without type
systems—even safe, dynamically checked languages — tend to offer features
or encourage programming idioms that make typechecking difficult or
infeasible*. Indeed, in typed languages the type system itself is often
taken as the foundation of the design and the organizing principle in
light of which every other aspect of the design is considered.

> A related point is that the relatively straightforward analyses embodied in
most type systems are not capable of proscribing arbitrary undesired
program behaviors; they can only guarantee that well-typed programs are
free from certain kinds of misbehavior. For example, most type systems can
check statically that the arguments to primitive arithmetic operations are
always numbers, that the receiver object in a method invocation always
provides the requested method, etc., but not that the second argument to
the division operation is non-zero, or that array accesses are always
within bounds.  The bad behaviors that can be eliminated by the type system
in a given language are often called *run-time type errors*. It is
important to keep in mind that this set of behaviors is a per-language
choice: although there is substantial overlap between the behaviors
considered to be run-time type errors in different languages, in principle
each type system comes with a definition of the behaviors it aims to
prevent. *The safety (or soundness) of each type system must be judged with
respect to its own set of run-time errors*.

> ... a *safe language* is one that protects its own abstractions. ...

> *Safety refers* to the language’s ability to guarantee the integrity of these
abstractions and of higher-level abstractions introduced by the programmer
using the definitional facilities of the language.

> *Language safety* is not the same thing as static type safety. Language safety
can be achieved by static checking, but also by run-time checks that trap
nonsensical operations just at the moment when they are attempted and stop
the program or raise an exception. For example, Scheme is a safe language,
even though *it has no static type system*.

> ... such languages (unsafe languages) do not qualify as type-safe either,
according to our definition, since they are generally not capable of
offering any sort of guarantees that well-typed programs are well
behaved—typecheckers for these languages can suggest the presence of
run-time type errors (which is certainly better than nothing) but not prove
their absence.

> Run-time safety is not normally achievable by static typing alone. For
example, all of the languages listed as safe in the table above actually
perform array-bounds checking dynamically.1 Similarly, statically checked
languages sometimes choose to provide operations (e.g., the down-cast
operator in Java—see) whose typechecking rules are actually
unsound—language safety is obtained by checking each use of such a
construct dynamically.

### L. Cardelli - Type Systems 

> The fundamental purpose of a type system is to prevent the occurrence of
*execution errors* during the running of a program. ... the absence of
execution errors is a nontrivial property.  When such a property holds for
all of the program runs that can be expressed within a programming
language, we say that the language is *type sound*. It turns out that a
fair amount of careful analysis is required to avoid false and embarrassing
claims of type soundness for programming languages. As a consequence, the
classification, description, and study of type systems has emerged as a
formal discipline.

> A *type system* is that component of a typed language that keeps track of the
types of variables and, in general, of the types of all expressions in a
program. Type systems are used to determine whether programs are well
behaved. Only program sources that comply with
a type system should be considered real programs of a typed language; the
other sources should be discarded before they are run.
    
> Languages where variables can be given (nontrivial) types are called *typed
languages*.  Languages that do not restrict the range of variables are
called *untyped languages*: they do not have types or, equivalently, have a
single universal type that contains all values. 

> Typed languages can enforce good behavior (including safety) by performing
*static (i.e., compile time) checks* to prevent unsafe and ill behaved
programs from ever running. These languages are *statically checked*; the
checking process is called *typechecking*, and the algorithm that performs
this checking is called the *typechecker*. A program that passes the
typechecker is said to be *well typed*; otherwise, it is *ill typed*, which may
mean that it is actually *ill-behaved*, or simply that it could not be
guaranteed to be well behaved. Examples of statically checked languages
are ML, Java, and Pascal (with the caveat that Pascal has some unsafe
features).

> Untyped languages can enforce good behavior (including safety) in a different
way, by performing sufficiently detailed run time checks to rule out all
forbidden errors. (For example, they may check all array bounds, and all
division operations, generating recoverable exceptions when forbidden errors
would happen.) The checking process in these languages is called *dynamic
checking*; LISP is an example of such a language. *These languages are strongly
checked even though they have neither static checking, nor a type system*.

> ... the declared goal of a type system is usually to ensure good behavior
of all programs, by distinguishing between well typed and ill typed
programs.

> Even statically checked languages usually need to perform tests at run time
to achieve safety. For example, array bounds must in general be tested
dynamically. The fact that a language is statically checked does not
necessarily mean that execution can proceed entirely blindly.

> Once a type system is formalized, we can attempt to prove a *type soundness
theorem stating that well-typed programs are well behaved*.  If such a
soundness theorem holds, we say that the type system is sound. (Good
behavior of all programs of a typed language and soundness of its type
system mean the same thing.)

Optimizations
-------------

### S. Hanov - Type inference using the Cartesian Product Algorithm on a dynamically typed language

> If the compiler can determine, for example, that a virtual method call
always resolves to the same method, then it can perform more
interprocedural optimizations, such as procedure inlining or elimination of
the virtual method dispatch.

### M. Salib - Faster than C: static type inference with Starkiller

> While compilation can improve performance, any such gains will be modest
unless the compiler can statically resolve most of the dynamism present in
source programs. Static type inference for Python programs would enable the
safe removal of most type checks and most instances of dynamic dispatch and
dynamic binding from the generated code. Removing dynamic dispatch and
binding leads to large performance benefits since their existence precludes
many traditional optimization techniques, such as inlining. 

### G. van Rossum - [The story of None, True and False (and an explanation of literals, keywords and builtins thrown in)](http://python-history.blogspot.ru/2013/11/story-of-none-true-false.html) 

> ... there was the concern (whether founded or not) that the way name lookup in
Python works, "evaluating" the expression None is slow, because it requires
at least two dictionary lookups (all names are looked up in the globals dict
before being looked up in the built-ins dict).

Polymorphism
------------

### O. Ageseen - The cartesian product algorithm

> Data polymorphism is the ability to store objects of different types in a
variable or slot. 

### M. Madsen - Type inference in Ruby using CPA

>Data Polymorphism: Refers to the ability of variables to hold objects of differ-
ent types. For example an instance variable might exhibit data polymor-
phism if it can contain objects of varying type.




