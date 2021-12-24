#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
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
	{ 0xa879d70c, "module_layout" },
	{ 0xeb233a45, "__kmalloc" },
	{ 0xf9a482f9, "msleep" },
	{ 0x999e8297, "vfree" },
	{ 0xb44ad4b3, "_copy_to_user" },
	{ 0x339551fe, "misc_register" },
	{ 0x7e526bfa, "__x86_indirect_thunk_r10" },
	{ 0xfb578fc5, "memset" },
	{ 0xebbe12f0, "current_task" },
	{ 0xc5850110, "printk" },
	{ 0x6626afca, "down" },
	{ 0xb601be4c, "__x86_indirect_thunk_rdx" },
	{ 0xc959d152, "__stack_chk_fail" },
	{ 0x8ddd8aad, "schedule_timeout" },
	{ 0x2ea2c95c, "__x86_indirect_thunk_rax" },
	{ 0xbdfb6dbb, "__fentry__" },
	{ 0xae04012c, "__vmalloc" },
	{ 0x37a0cba, "kfree" },
	{ 0x69acdf38, "memcpy" },
	{ 0xedc03953, "iounmap" },
	{ 0xcf2a6966, "up" },
	{ 0x556422b3, "ioremap_cache" },
	{ 0x362ef408, "_copy_from_user" },
	{ 0x8ebf6186, "misc_deregister" },
	{ 0x88db9f48, "__check_object_size" },
	{ 0x81e6b37f, "dmi_get_system_info" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "D247A978ACC2B361777B284");
