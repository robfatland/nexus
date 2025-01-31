[nexus](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md), 
[nexus main branch](https://github.com/robfatland/nexus/tree/main)


[Study on ML implementation using preemptible VMs](https://github.com/oorjitchowdhary/ml-training-preemptible-vms/blob/main/README.md)


# spot: Preemptible cloud Virtual Machines, 70-90% savings


The spot market exists on all three clouds: "Spot Virtual Machines" represent excess capacity made available 
at a reduced rate. For research applications -- once we understand the ground rules -- the spot market makes
sense as a way of saving 50 to 90 percent of the on-demand price. Taking these two extremes we can say this
is equivalent to spending $10,000 and getting $20,000 to $100,000 worth of processing. But of course there is
a catch: These instances can go away on very short notice (2 minutes) so to make effective use of them there 
is a necessary learning process. 


If you look into the Spot Market material presented by the vendors (AWS and so on) you are bombarded with
a lot of jargon around scale and elasticity: Terms like "load balancing" and "fleet" and so on. The narrative
on this page will try and throttle back the service jargon and stick with basic operating ideas for 
using spot markets. 


