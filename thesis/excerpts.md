Dynamic typing vs. Static typing
--------------------------------
G. Steel (referenced by M. Furr, B. Cannon)

    A dynamic language is one that defers as many decisions as possible to
    runtime.
    

M. Furr - Static Type Inference in Ruby:

    Dynamic typing is appealing because it ensures that no correct program exe-
    cution is stopped prematurely—only programs about to “go wrong” at run time
    are rejected.

    Moreover, with pure dynamic typing, programmers lose the con-
    cise, automatically-checked documentation provided by type anno-
    tations.

F. Ortin - Union and intersection types to support both dynamic and static typing

    Static typing is an unquestionably important tool for software development,
    offering the programmer advan- tages such as early type error detection,
    better documen- tation and abstraction, and more opportunities for com-
    piler optimizations. Nevertheless, dynamically typed lan- guages provide
    great flexibility at runtime, making them ideally suited for prototyping
    systems with changing or unknown requirements, or which interact with other
    sys- tems that change unpredictably (data and application inte- gration)

S. Tu - MINO: Data-driven approximate type inference for Python

    Dynamic programming languages, such as Python and Ruby, are
    becoming the languages of choice for many developers. The lack
    of strict compile-time type checking is often cited as making de-
    velopment cycles faster. However, a big drawback to dynamically
    typed languages is that it is impossible to know the exact type of
    a given variable at compile time; it is a well known result that this
    problem is undecidable for such languages

J. Aycock - Aggressive Type Inference
    
    Python is a "dynamically typed" language because, in general, 
    the type of any variable is not known definitively until run-time.
    
    Giviving people a dynamically-typed language does not mean that they 
    write dynamically typed programs.

E. Maya - A Static Type Inference for Python

    Dynamic languages, like Python, are attractive because they
    guarantee that no correct program is rejected prematurely.
    However, this comes at a price of losing early error detection,
    and making both code optimization and certification harder
    tasks when compared with static typed languages. 

    However, when time performance is not absolutely critical, the speed and
    simplicity of the devel- opment cycle and the safety and clarity of the
    code justify the use of high-level languages, such as Python.

    Python is dynamically typed and allows variables to take values of different
    types in different program places. 

S. Hanov - Type inference using the Cartesian Product Algorithm on a
dynamically typed language
   
   ... duck-typed languages--languages for which the variables are bound to
   types when they are assigned a value. In these languages, it is not even
   obvious to the programmer if calling a method will work, and any extra
   information that can be gleaned by the compiler would be helpful.

A. Holkner - Evaluating the dynamic behaviour of Python applications
    
    The Python programming language is typical among dynamic languages in that
    programs written in it are not susceptible to static analysis. This makes
    effi- cient static program compilation difficult, as well as limiting the
    amount of early error detection that can be performed.

Duck typing
-----------

F. Ortin - Union and intersection types to support both dynamic and static typing

    Duck typing is a property offered by most dynamically typed
    languages that means that an object is interchangeable with any other
    object that implements the same dynamic interface, regardless of whether
    those objects have a related inheritance hierarchy or not.


S. Hanov - Type inference using the Cartesian Product Algorithm on a
dynamically typed language

    Dynamically typed, (or “duck typed”) languages are useful for
    rapid prototyping and code reuse. In languages that have duck
    typing, a variable’s value determines what it can do, and implies
    that an object is interchangeable with any other object that
    implements the same interface, regardless of whether the objects
    are related by inheritance.


Type inference
--------------

M. Salib - Faster than C: static type inference with Starkiller

    From a type inference perspective, Python is a large and complex language.
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

B. Pierce - Types and programming languages

    A type system is a tractable syntactic method for proving the absence of
    certain program behaviors by classifying phrases according to the kinds of
    values they compute.

    Retrofitting a type system onto a language not designed with typechecking
    in mind can be tricky; ideally, language design should go hand-in-hand with
    type system design.  One reason for this is that languages without type
    systems—even safe, dy- namically checked languages—tend to offer features
    or encourage program- ming idioms that make typechecking difficult or
    infeasible. Indeed, in typed languages the type system itself is often
    taken as the foundation of the de- sign and the organizing principle in
    light of which every other aspect of the design is considered.


Optimizations
-------------

S. Hanov - Type inference using the Cartesian Product Algorithm on a
dynamically typed language

    If the compiler can determine, for example, that a virtual method call
    always resolves to the same method, then it can perform more
    interprocedural optimizations, such as procedure inlining or elimination of
    the virtual method dispatch.

M. Salib - Faster than C: static type inference with Starkiller

    While compilation can improve performance, any such gains will be modest
    unless the compiler can statically resolve most of the dynamism present in
    source programs. Static type inference for Python programs would enable the
    safe removal of most type checks and most instances of dynamic dispatch and
    dynamic binding from the generated code. Removing dynamic dispatch and
    binding leads to large performance benefits since their existence precludes
    many traditional optimization techniques, such as inlining. 




