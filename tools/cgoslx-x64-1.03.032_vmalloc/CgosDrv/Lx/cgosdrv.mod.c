#include <linux/build-salt.h>
#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(.gnu.linkonce.this_module) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used __section(__versions) = {
	{ 0x64491f21, "module_layout" },
	{ 0xeb233a45, "__kmalloc" },
	{ 0xdf566a59, "__x86_indirect_thunk_r9" },
	{ 0x999e8297, "vfree" },
	{ 0xb44ad4b3, "_copy_to_user" },
	{ 0x30c36813, "misc_register" },
	{ 0xfb578fc5, "memset" },
	{ 0xd38cd261, "__default_kernel_pte_mask" },
	{ 0x3e4faeee, "current_task" },
	{ 0x6626afca, "down" },
	{ 0xdecd0b29, "__stack_chk_fail" },
	{ 0x8ddd8aad, "schedule_timeout" },
	{ 0x2ea2c95c, "__x86_indirect_thunk_rax" },
	{ 0xbdfb6dbb, "__fentry__" },
	{ 0x7812c047, "__vmalloc" },
	{ 0x37a0cba, "kfree" },
	{ 0x69acdf38, "memcpy" },
	{ 0xedc03953, "iounmap" },
	{ 0xcf2a6966, "up" },
	{ 0x556422b3, "ioremap_cache" },
	{ 0x362ef408, "_copy_from_user" },
	{ 0x148101c9, "misc_deregister" },
	{ 0x88db9f48, "__check_object_size" },
	{ 0x8a35b432, "sme_me_mask" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "8BEFEF61157E1ECEF4D1E44");
