type DiningPhilosophers struct {
    mu sync.Mutex
    cond *sync.Cond
    forks [5]bool
}

func (this *DiningPhilosophers) wantsToEat(
    philosopher int,
    pickLeftFork func(),
    pickRightFork func(),
    eat func(),
    putLeftFork func(),
    putRightFork func(),
) {
    this.mu.Lock()
    if this.cond == nil{
        this.cond = sync.NewCond(&this.mu)
        for i:= range this.forks{
            this.forks[i]=true
        }
    }
    left := philosopher 
    right :=(philosopher+1)%5
    for !this.forks[left] || !this.forks[right]{
        this.cond.Wait()
    }
    this.forks[left]=false
    this.forks[right]=false
    pickLeftFork()
    pickRightFork()
    this.mu.Unlock()
    eat()
    this.mu.Lock()
    this.forks[left]=true
    this.forks[right]=true
    putLeftFork()
    putRightFork()
    this.cond.Broadcast()
    this.mu.Unlock()

}

