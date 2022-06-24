cmd_/home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../CgosDrv.o := gcc -Wp,-MD,/home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../.CgosDrv.o.d  -nostdinc -isystem /usr/lib/gcc/x86_64-linux-gnu/9/include  -I./arch/x86/include -I./arch/x86/include/generated  -I./include -I./arch/x86/include/uapi -I./arch/x86/include/generated/uapi -I./include/uapi -I./include/generated/uapi -include ./include/linux/kconfig.h -Iubuntu/include  -include ./include/linux/compiler_types.h -D__KERNEL__ -Wall -Wundef -Werror=strict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -fshort-wchar -fno-PIE -Werror=implicit-function-declaration -Werror=implicit-int -Werror=return-type -Wno-format-security -std=gnu89 -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -fcf-protection=none -m64 -falign-jumps=1 -falign-loops=1 -mno-80387 -mno-fp-ret-in-387 -mpreferred-stack-boundary=3 -mskip-rax-setup -mtune=generic -mno-red-zone -mcmodel=kernel -DCONFIG_X86_X32_ABI -DCONFIG_AS_CFI=1 -DCONFIG_AS_CFI_SIGNAL_FRAME=1 -DCONFIG_AS_CFI_SECTIONS=1 -DCONFIG_AS_SSSE3=1 -DCONFIG_AS_AVX=1 -DCONFIG_AS_AVX2=1 -DCONFIG_AS_AVX512=1 -DCONFIG_AS_SHA1_NI=1 -DCONFIG_AS_SHA256_NI=1 -Wno-sign-compare -fno-asynchronous-unwind-tables -mindirect-branch=thunk-extern -mindirect-branch-register -fno-jump-tables -fno-delete-null-pointer-checks -Wno-frame-address -Wno-format-truncation -Wno-format-overflow -Wno-address-of-packed-member -O2 --param=allow-store-data-races=0 -Wframe-larger-than=1024 -fstack-protector-strong -Wimplicit-fallthrough -Wno-unused-but-set-variable -Wno-unused-const-variable -fno-omit-frame-pointer -fno-optimize-sibling-calls -fno-var-tracking-assignments -pg -mrecord-mcount -mfentry -DCC_USING_FENTRY -flive-patching=inline-clone -Wdeclaration-after-statement -Wvla -Wno-pointer-sign -Wno-stringop-truncation -Wno-array-bounds -Wno-stringop-overflow -Wno-restrict -Wno-maybe-uninitialized -fno-strict-overflow -fno-merge-all-constants -fmerge-constants -fno-stack-check -fconserve-stack -Werror=date-time -Werror=incompatible-pointer-types -Werror=designated-init -fmacro-prefix-map=./= -Wno-packed-not-aligned -I/home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/. -I/home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/.. -I/home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../../CgosLib -I/home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../../CgosLib/Lx -O2 -fno-strict-aliasing -I/home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../..  -DMODULE  -DKBUILD_BASENAME='"CgosDrv"' -DKBUILD_MODNAME='"cgosdrv"' -c -o /home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../CgosDrv.o /home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../CgosDrv.c

source_/home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../CgosDrv.o := /home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../CgosDrv.c

deps_/home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../CgosDrv.o := \
  include/linux/kconfig.h \
    $(wildcard include/config/cpu/big/endian.h) \
    $(wildcard include/config/booger.h) \
    $(wildcard include/config/foo.h) \
  include/linux/compiler_types.h \
    $(wildcard include/config/have/arch/compiler/h.h) \
    $(wildcard include/config/enable/must/check.h) \
    $(wildcard include/config/optimize/inlining.h) \
    $(wildcard include/config/cc/has/asm/inline.h) \
  include/linux/compiler_attributes.h \
  include/linux/compiler-gcc.h \
    $(wildcard include/config/arm64.h) \
    $(wildcard include/config/retpoline.h) \
    $(wildcard include/config/arch/use/builtin/bswap.h) \
  /home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../CgosDrv.h \
  /home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/./DrvOsHdr.h \
  /home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../../CgosLib/CgosDef.h \
  /home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../../CgosLib/Cgos.h \
  /home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../../CgosLib/CgosPriv.h \
  /home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../../CgosLib/CgosIoct.h \
  /home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../Cgeb.h \
  /home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../CgebSda.h \
  /home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../DrvVars.h \
  /home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../DrvUla.h \
  /home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../DrvOsa.h \
  /home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../CgebFct.h \
  /home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../../CgosBld.h \

/home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../CgosDrv.o: $(deps_/home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../CgosDrv.o)

$(deps_/home/stux/cgoslx-x64-1.03.032/CgosDrv/Lx/../CgosDrv.o):
