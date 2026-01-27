[nexus published](https://robfatland.github.io/nexus), [index source](https://github.com/robfatland/nexus/blob/gh-pages/index.md)


# gcp


The Google Cloud Platform (gcp) has some excellent features. Also, like with other cloud platforms, there are managed and
un-managed versions of services. Here we annotate the process of setting up RStudio on an unmanaged VM (GCP jargon: 
"Compute Engine").


- Log in to https://console.cloud.google.com; and be sure to choose the intended *project*
    - The following steps can be done using the GCP Command Line Interface (CLI) which is called `gcloud`
- GCP console: Create a VM
    - In the Console the Wizard has about 7 stages (left sidebar)
    - We have very little to do here, really only on the first and second stages
    - First stage: Chose a clear purpose-specific name for the VM
        - Chose the closest possible region e.g. `us-west1` for Oregon. Leave Zone as `any`.
        - Instance type: Select `E2`; specifically e2-medium. This will run about $25/month
    - Do not jump the queue by clicking the **Create** button; there is more to be done
    - Do click the second page (left sidebar) to chose OS and Storage
        - Change the operating system: Select a current version of Ubuntu; the rest default
    - Go to the next tab: Data Protection. Consider the options that suit your project.
        - If you regularly commit your code to GitHub then this is redundant
        - If your data / results are expensive to reproduce: Read more about Backups and Snapshots
    - Go to the fourth tab: Networking
        - Do not change anything here; just note the Firewall options for context
        - The eventual idea will be to open port 8787 for `tcp` traffic to support RStudio
    - 
