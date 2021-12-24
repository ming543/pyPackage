#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);

struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
 .name = KBUILD_MODNAME,
 .init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
 .exit = cleanup_module,
#endif
 .arch = MODULE_ARCH_INIT,
};

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0x7d09bae2, "module_layout" },
	{ 0xa3247381, "per_cpu__current_task" },
	{ 0x12da5bb2, "__kmalloc" },
	{ 0x999e8297, "vfree" },
	{ 0xfddfb507, "misc_register" },
	{ 0x2f287f0d, "copy_to_user" },
	{ 0xb4390f9a, "mcount" },
	{ 0x748caf40, "down" },
	{ 0xf0fdf6cb, "__stack_chk_fail" },
	{ 0xd62c833f, "schedule_timeout" },
	{ 0xa9bd2676, "__vmalloc" },
	{ 0x37a0cba, "kfree" },
	{ 0xedc03953, "iounmap" },
	{ 0x3f1899f1, "up" },
	{ 0xeff14be9, "ioremap_cache" },
	{ 0xd6c963c, "copy_from_user" },
	{ 0x58ab334a, "misc_deregister" },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=";

