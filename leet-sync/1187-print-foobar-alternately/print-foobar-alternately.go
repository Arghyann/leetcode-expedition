type FooBar struct {
	n int
    foo chan int
    bar chan int 
}

func NewFooBar(n int) *FooBar {
	fb:= &FooBar{
        n: n,
        foo: make(chan int,1),
        bar: make(chan int,1),
        }
        fb.foo <- 1 
    return fb
}

func (fb *FooBar) Foo(printFoo func()) {
	for i := 0; i < fb.n; i++ {
        <-fb.foo
		// printFoo() outputs "foo". Do not change or remove this line.
        printFoo()
        fb.bar<-1
	}
}

func (fb *FooBar) Bar(printBar func()) {
	for i := 0; i < fb.n; i++ {
        <-fb.bar
		// printBar() outputs "bar". Do not change or remove this line.
        printBar()
        fb.foo<-1
	}
}