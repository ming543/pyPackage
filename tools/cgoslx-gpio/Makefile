ALLDIRS = CgosDrv CgosLib CgosI2cGpio

# Determination of the target system
target = $(shell uname)
sysdir = Lx

ifdef target
 ifeq ("$(target)","QNX")
  sysdir = Qx
 endif
endif

M = for i in $(ALLDIRS); do make -C $$i/$(sysdir)
N = || exit 1; done

ifeq ("$(target)","QNX")
install:
	cp CgosI2cGpio/$(sysdir)/cgosi2c_gpio /usr/bin
	cp CgosLib/$(sysdir)/libcgos.so /usr/lib
	cp CgosDrv/$(sysdir)/cgosdrv /usr/lib
else

default:
	$(M) $(N)

install:
	install -m 755 -o root -g root CgosI2cGpio/$(sysdir)/cgosi2c_gpio /usr/bin
	install -m 755 -o root -g root CgosLib/$(sysdir)/libcgos.so /usr/lib
	$(MAKE) -C CgosDrv/$(sysdir) install

clean:
	$(M) $@ $(N)

endif



