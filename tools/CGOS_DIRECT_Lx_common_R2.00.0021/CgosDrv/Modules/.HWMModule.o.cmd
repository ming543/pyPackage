cmd_/home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../Modules/HWMModule.o := gcc -Wp,-MMD,/home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../Modules/.HWMModule.o.d  -nostdinc -isystem /usr/lib/gcc/x86_64-linux-gnu/9/include  -I./arch/x86/include -I./arch/x86/include/generated  -I./include -I./arch/x86/include/uapi -I./arch/x86/include/generated/uapi -I./include/uapi -I./include/generated/uapi -include ./include/linux/kconfig.h -Iubuntu/include  -include ./include/linux/compiler_types.h -D__KERNEL__ -Wall -Wundef -Werror=strict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -fshort-wchar -fno-PIE -Werror=implicit-function-declaration -Werror=implicit-int -Werror=return-type -Wno-format-security -std=gnu89 -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -fcf-protection=none -m64 -falign-jumps=1 -falign-loops=1 -mno-80387 -mno-fp-ret-in-387 -mpreferred-stack-boundary=3 -mskip-rax-setup -mtune=generic -mno-red-zone -mcmodel=kernel -DCONFIG_X86_X32_ABI -Wno-sign-compare -fno-asynchronous-unwind-tables -mindirect-branch=thunk-extern -mindirect-branch-register -fno-jump-tables -fno-delete-null-pointer-checks -Wno-frame-address -Wno-format-truncation -Wno-format-overflow -Wno-address-of-packed-member -O2 --param=allow-store-data-races=0 -Wframe-larger-than=1024 -fstack-protector-strong -Wno-unused-but-set-variable -Wimplicit-fallthrough -Wno-unused-const-variable -fno-omit-frame-pointer -fno-optimize-sibling-calls -fno-var-tracking-assignments -pg -mrecord-mcount -mfentry -DCC_USING_FENTRY -Wdeclaration-after-statement -Wvla -Wno-pointer-sign -Wno-stringop-truncation -Wno-array-bounds -Wno-stringop-overflow -Wno-restrict -Wno-maybe-uninitialized -fno-strict-overflow -fno-merge-all-constants -fmerge-constants -fno-stack-check -fconserve-stack -Werror=date-time -Werror=incompatible-pointer-types -Werror=designated-init -fmacro-prefix-map=./= -Wno-packed-not-aligned -I/home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/. -I/home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/.. -I/home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../../CgosLib -I/home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../../CgosLib/Lx -O2 -fno-strict-aliasing -I/home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../..  -DMODULE  -DKBUILD_BASENAME='"HWMModule"' -DKBUILD_MODNAME='"cgosdrv"' -c -o /home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../Modules/HWMModule.o /home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../Modules/HWMModule.c

source_/home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../Modules/HWMModule.o := /home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../Modules/HWMModule.c

deps_/home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../Modules/HWMModule.o := \
  include/linux/kconfig.h \
    $(wildcard include/config/cc/version/text.h) \
    $(wildcard include/config/cpu/big/endian.h) \
    $(wildcard include/config/booger.h) \
    $(wildcard include/config/foo.h) \
  include/linux/compiler_types.h \
    $(wildcard include/config/have/arch/compiler/h.h) \
    $(wildcard include/config/enable/must/check.h) \
    $(wildcard include/config/cc/has/asm/inline.h) \
  include/linux/compiler_attributes.h \
  include/linux/compiler-gcc.h \
    $(wildcard include/config/arm64.h) \
    $(wildcard include/config/retpoline.h) \
    $(wildcard include/config/arch/use/builtin/bswap.h) \
  include/linux/printk.h \
    $(wildcard include/config/message/loglevel/default.h) \
    $(wildcard include/config/console/loglevel/default.h) \
    $(wildcard include/config/console/loglevel/quiet.h) \
    $(wildcard include/config/early/printk.h) \
    $(wildcard include/config/printk/nmi.h) \
    $(wildcard include/config/printk.h) \
    $(wildcard include/config/kmsg/ids.h) \
    $(wildcard include/config/dynamic/debug.h) \
    $(wildcard include/config/dynamic/debug/core.h) \
  include/linux/init.h \
    $(wildcard include/config/have/arch/prel32/relocations.h) \
    $(wildcard include/config/strict/kernel/rwx.h) \
    $(wildcard include/config/strict/module/rwx.h) \
  include/linux/compiler.h \
    $(wildcard include/config/trace/branch/profiling.h) \
    $(wildcard include/config/profile/all/branches.h) \
    $(wildcard include/config/stack/validation.h) \
    $(wildcard include/config/debug/entry.h) \
  include/linux/compiler_types.h \
  arch/x86/include/asm/barrier.h \
    $(wildcard include/config/x86/32.h) \
  arch/x86/include/asm/alternative.h \
    $(wildcard include/config/smp.h) \
  include/linux/types.h \
    $(wildcard include/config/have/uid16.h) \
    $(wildcard include/config/uid16.h) \
    $(wildcard include/config/arch/dma/addr/t/64bit.h) \
    $(wildcard include/config/phys/addr/t/64bit.h) \
    $(wildcard include/config/64bit.h) \
  include/uapi/linux/types.h \
  arch/x86/include/generated/uapi/asm/types.h \
  include/uapi/asm-generic/types.h \
  include/asm-generic/int-ll64.h \
  include/uapi/asm-generic/int-ll64.h \
  arch/x86/include/uapi/asm/bitsperlong.h \
  include/asm-generic/bitsperlong.h \
  include/uapi/asm-generic/bitsperlong.h \
  include/uapi/linux/posix_types.h \
  include/linux/stddef.h \
  include/uapi/linux/stddef.h \
  arch/x86/include/asm/posix_types.h \
  arch/x86/include/uapi/asm/posix_types_64.h \
  include/uapi/asm-generic/posix_types.h \
  include/linux/stringify.h \
  arch/x86/include/asm/asm.h \
  arch/x86/include/asm/nops.h \
    $(wildcard include/config/mk7.h) \
    $(wildcard include/config/x86/p6/nop.h) \
    $(wildcard include/config/x86/64.h) \
  include/asm-generic/barrier.h \
  include/linux/kasan-checks.h \
    $(wildcard include/config/kasan.h) \
  include/linux/kcsan-checks.h \
    $(wildcard include/config/kcsan.h) \
    $(wildcard include/config/kcsan/ignore/atomics.h) \
  include/linux/kern_levels.h \
  include/linux/linkage.h \
    $(wildcard include/config/arch/use/sym/annotations.h) \
  include/linux/export.h \
    $(wildcard include/config/modversions.h) \
    $(wildcard include/config/module/rel/crcs.h) \
    $(wildcard include/config/modules.h) \
    $(wildcard include/config/trim/unused/ksyms.h) \
    $(wildcard include/config/unused/symbols.h) \
  arch/x86/include/asm/linkage.h \
    $(wildcard include/config/x86/alignment/16.h) \
  include/linux/cache.h \
    $(wildcard include/config/arch/has/cache/line/size.h) \
  include/uapi/linux/kernel.h \
  include/uapi/linux/sysinfo.h \
  include/linux/const.h \
  include/vdso/const.h \
  include/uapi/linux/const.h \
  arch/x86/include/asm/cache.h \
    $(wildcard include/config/x86/l1/cache/shift.h) \
    $(wildcard include/config/x86/internode/cache/shift.h) \
    $(wildcard include/config/x86/vsmp.h) \
  include/linux/dynamic_debug.h \
    $(wildcard include/config/jump/label.h) \
  include/linux/jump_label.h \
    $(wildcard include/config/have/arch/jump/label/relative.h) \
  arch/x86/include/asm/jump_label.h \
  /home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../CgosDrv.h \
  /home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/./DrvOsHdr.h \
  /home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../CgosDef.h \
  /home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../../CgosLib/Cgos.h \
  /home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../../CgosLib/CgosPriv.h \
  /home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../../CgosLib/CgosIoct.h \
  /home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../Cgeb.h \
  /home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../DrvVars.h \
  /home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../DrvUla.h \
  /home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../DrvOsa.h \
  /home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../Modules/BCModule.h \
  /home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../Modules/HWMModule_cfg.h \
  /home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../Modules/HWMSubModules/HWMSubModule_BC.h \

/home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../Modules/HWMModule.o: $(deps_/home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../Modules/HWMModule.o)

$(deps_/home/stux/CGOS_DIRECT_Lx_common_R2.00.0021/CgosDrv/Lx/../Modules/HWMModule.o):
