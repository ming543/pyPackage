This CGOS driver package version uses a modified vmalloc function which will only work with a Kernel patched with cgos_vmalloc.patch.

Build instructions:


* copy the cgos_vmalloc.patch from the CGOS driver package root directory to /usr/src/kernels:

cp cgos_vmalloc.patch /usr/src/kernels


* Make sure that user root is authorized for signing

/usr/libexec/pesign/pesign-authorize


* Change to Kernel source directory

cd /usr/src/kernels


* Get Vanilla Kernel matching the Kernel Version currently running

wget https://mirrors.edge.kernel.org/pub/linux/kernel/v$(uname -r | cut -f1 -d'.').x/linux-$(uname -r | cut -f1 -d'-').tar.gz


* Unpack the Kernel sources

tar -xzf linux-$(uname -r | cut -f1 -d'-').tar.gz


* Go to the directory with the Kernel sources

cd linux-$(uname -r | cut -f1 -d'-')


* Apply the cgos_vmalloc Kernel patch

patch -p1 < ../cgos_vmalloc.patch


* Optional: Get the current distribution configuration....

cp /boot/config-$(uname -r | cut -f1 -d'-')* .config


* Optional: ... and restore the distribution config

yes '' | make oldconfig


* Optional: add extra version string to the line EXTRAVERSION = in the Makefile of the Kernel source root directory
  in order to be able to identify the new kernel,  for example EXTRAVERSION = -cgos-patch


* Build and install Kernel:

sudo make
sudo make modules_install
sudo make install
