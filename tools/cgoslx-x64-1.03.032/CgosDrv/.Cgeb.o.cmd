cmd_/home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../Cgeb.o :=  gcc-10 -Wp,-MMD,/home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../.Cgeb.o.d -nostdinc -isystem /usr/lib/gcc/x86_64-linux-gnu/10/include -I/usr/src/linux-headers-5.10.0-16-common/arch/x86/include -I./arch/x86/include/generated -I/usr/src/linux-headers-5.10.0-16-common/include -I./include -I/usr/src/linux-headers-5.10.0-16-common/arch/x86/include/uapi -I./arch/x86/include/generated/uapi -I/usr/src/linux-headers-5.10.0-16-common/include/uapi -I./include/generated/uapi -include /usr/src/linux-headers-5.10.0-16-common/include/linux/kconfig.h -include /usr/src/linux-headers-5.10.0-16-common/include/linux/compiler_types.h -D__KERNEL__ -fmacro-prefix-map=/usr/src/linux-headers-5.10.0-16-common/= -Wall -Wundef -Werror=strict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -fshort-wchar -fno-PIE -Werror=implicit-function-declaration -Werror=implicit-int -Werror=return-type -Wno-format-security -std=gnu89 -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -fcf-protection=none -m64 -falign-jumps=1 -falign-loops=1 -mno-80387 -mno-fp-ret-in-387 -mpreferred-stack-boundary=3 -mskip-rax-setup -mtune=generic -mno-red-zone -mcmodel=kernel -DCONFIG_X86_X32_ABI -Wno-sign-compare -fno-asynchronous-unwind-tables -mindirect-branch=thunk-extern -mindirect-branch-register -fno-jump-tables -fno-delete-null-pointer-checks -Wno-frame-address -Wno-format-truncation -Wno-format-overflow -Wno-address-of-packed-member -O2 -fno-allow-store-data-races -Wframe-larger-than=2048 -fstack-protector-strong -Wimplicit-fallthrough -Wno-unused-but-set-variable -Wno-unused-const-variable -g -pg -mrecord-mcount -mfentry -DCC_USING_FENTRY -Wdeclaration-after-statement -Wvla -Wno-pointer-sign -Wno-stringop-truncation -Wno-zero-length-bounds -Wno-array-bounds -Wno-stringop-overflow -Wno-restrict -Wno-maybe-uninitialized -fno-strict-overflow -fno-stack-check -fconserve-stack -Werror=date-time -Werror=incompatible-pointer-types -Werror=designated-init -Wno-packed-not-aligned -I/home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/. -I/home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/.. -I/home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../../CgosLib -I/home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../../CgosLib/Lx -O2 -fno-strict-aliasing -I/home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../..  -DMODULE  -DKBUILD_BASENAME='"Cgeb"' -DKBUILD_MODNAME='"cgosdrv"' -c -o /home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../Cgeb.o /home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../Cgeb.c

source_/home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../Cgeb.o := /home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../Cgeb.c

deps_/home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../Cgeb.o := \
  /usr/src/linux-headers-5.10.0-16-common/include/linux/kconfig.h \
    $(wildcard include/config/cc/version/text.h) \
    $(wildcard include/config/cpu/big/endian.h) \
    $(wildcard include/config/booger.h) \
    $(wildcard include/config/foo.h) \
  /usr/src/linux-headers-5.10.0-16-common/include/linux/compiler_types.h \
    $(wildcard include/config/have/arch/compiler/h.h) \
    $(wildcard include/config/enable/must/check.h) \
    $(wildcard include/config/cc/has/asm/inline.h) \
  /usr/src/linux-headers-5.10.0-16-common/include/linux/compiler_attributes.h \
  /usr/src/linux-headers-5.10.0-16-common/include/linux/compiler-gcc.h \
    $(wildcard include/config/arm64.h) \
    $(wildcard include/config/retpoline.h) \
    $(wildcard include/config/arch/use/builtin/bswap.h) \
    $(wildcard include/config/kcov.h) \
  /usr/src/linux-headers-5.10.0-16-common/include/linux/types.h \
    $(wildcard include/config/have/uid16.h) \
    $(wildcard include/config/uid16.h) \
    $(wildcard include/config/arch/dma/addr/t/64bit.h) \
    $(wildcard include/config/phys/addr/t/64bit.h) \
    $(wildcard include/config/64bit.h) \
  /usr/src/linux-headers-5.10.0-16-common/include/uapi/linux/types.h \
  arch/x86/include/generated/uapi/asm/types.h \
  /usr/src/linux-headers-5.10.0-16-common/include/uapi/asm-generic/types.h \
  /usr/src/linux-headers-5.10.0-16-common/include/asm-generic/int-ll64.h \
  /usr/src/linux-headers-5.10.0-16-common/include/uapi/asm-generic/int-ll64.h \
  /usr/src/linux-headers-5.10.0-16-common/arch/x86/include/uapi/asm/bitsperlong.h \
  /usr/src/linux-headers-5.10.0-16-common/include/asm-generic/bitsperlong.h \
  /usr/src/linux-headers-5.10.0-16-common/include/uapi/asm-generic/bitsperlong.h \
  /usr/src/linux-headers-5.10.0-16-common/include/uapi/linux/posix_types.h \
  /usr/src/linux-headers-5.10.0-16-common/include/linux/stddef.h \
  /usr/src/linux-headers-5.10.0-16-common/include/uapi/linux/stddef.h \
  /usr/src/linux-headers-5.10.0-16-common/include/linux/compiler_types.h \
  /usr/src/linux-headers-5.10.0-16-common/arch/x86/include/asm/posix_types.h \
    $(wildcard include/config/x86/32.h) \
  /usr/src/linux-headers-5.10.0-16-common/arch/x86/include/uapi/asm/posix_types_64.h \
  /usr/src/linux-headers-5.10.0-16-common/include/uapi/asm-generic/posix_types.h \
  /home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../CgosDrv.h \
  /home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/./DrvOsHdr.h \
  /home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../../CgosLib/CgosDef.h \
  /home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../../CgosLib/Cgos.h \
  /home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../../CgosLib/CgosPriv.h \
  /home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../../CgosLib/CgosIoct.h \
  /home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../Cgeb.h \
  /home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../CgebSda.h \
  /home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../DrvVars.h \
  /home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../DrvUla.h \
  /home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../DrvOsa.h \
  /home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../CgebFct.h \

/home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../Cgeb.o: $(deps_/home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../Cgeb.o)

$(deps_/home/stux/pyPackage/tools/cgoslx-x64-1.03.032/CgosDrv/Lx/../Cgeb.o):
