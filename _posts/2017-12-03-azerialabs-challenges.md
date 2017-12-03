---
title: "AzeriaLabs Challenges - Stack1"
excerpt: Summary for challenge Stack1
categories:
  - CTF
tags:
  - CTF
  - AzeriaLabs
comments: true
---

{% include toc %}

# 背景


最近学习了 https://azeria-labs.com/ 出的ARM Exploit教程，最后作者出了几个挑战题目，以下是的解题思路。

**（题目很简单，大神勿喷）**

题目在这： https://azeria-labs.com/part-3-stack-overflow-challenges/

# 环境

1. 直接使用作者提供的虚拟机 https://azeria-labs.com/arm-lab-vm/
2. armv6 树莓派

# 题目 Stack1

```
What you will learn

How to modify variables to specific values in the program
How the variables are laid out in memory
Goal: Change the ‘modified’ variable. You solved the challenge once “You have changed the ‘modified’ variable” is printed out.
```

## 初步运行

先直接运行看看，

```
pi@raspberrypi:~/ARM-challenges $ ./stack1
stack1: please specify an argument
```

那就加个参数

```
pi@raspberrypi:~/ARM-challenges $ ./stack1 1111111111111111
Try again, you got 0x00000000
```

再参数长点

```
pi@raspberrypi:~/ARM-challenges $ ./stack1 111111111111111111111111111111111111111111111111111111111111111111111111111111
Try again, you got 0x31313131
Segmentation fault
```

哇，数值变了。0x31就是1啦。而且crash了。

## 调试

```
gdb stack1
break main
run
```

输出汇编

```
gef> disassemble main
Dump of assembler code for function main:
=> 0x000104b0 <+0>:	push	{r11, lr}
   0x000104b4 <+4>:	add	r11, sp, #4
   0x000104b8 <+8>:	sub	sp, sp, #80	; 0x50
   0x000104bc <+12>:	str	r0, [r11, #-80]	; 0x50
   0x000104c0 <+16>:	str	r1, [r11, #-84]	; 0x54
   0x000104c4 <+20>:	ldr	r3, [r11, #-80]	; 0x50
   0x000104c8 <+24>:	cmp	r3, #1
   0x000104cc <+28>:	bne	0x104dc <main+44>
   0x000104d0 <+32>:	mov	r0, #1
   0x000104d4 <+36>:	ldr	r1, [pc, #92]	; 0x10538 <main+136>
   0x000104d8 <+40>:	bl	0x10370
   0x000104dc <+44>:	mov	r3, #0
   0x000104e0 <+48>:	str	r3, [r11, #-8]
   0x000104e4 <+52>:	ldr	r3, [r11, #-84]	; 0x54
   0x000104e8 <+56>:	add	r3, r3, #4
   0x000104ec <+60>:	ldr	r3, [r3]
   0x000104f0 <+64>:	sub	r2, r11, #72	; 0x48
   0x000104f4 <+68>:	mov	r0, r2
   0x000104f8 <+72>:	mov	r1, r3
   0x000104fc <+76>:	bl	0x10340
   0x00010500 <+80>:	ldr	r3, [r11, #-8]
   0x00010504 <+84>:	ldr	r2, [pc, #48]	; 0x1053c <main+140>
   0x00010508 <+88>:	cmp	r3, r2
   0x0001050c <+92>:	bne	0x1051c <main+108>
   0x00010510 <+96>:	ldr	r0, [pc, #40]	; 0x10540 <main+144>
   0x00010514 <+100>:	bl	0x1034c
   0x00010518 <+104>:	b	0x1052c <main+124>
   0x0001051c <+108>:	ldr	r3, [r11, #-8]
   0x00010520 <+112>:	ldr	r0, [pc, #28]	; 0x10544 <main+148>
   0x00010524 <+116>:	mov	r1, r3
   0x00010528 <+120>:	bl	0x10334
   0x0001052c <+124>:	mov	r0, r3
   0x00010530 <+128>:	sub	sp, r11, #4
   0x00010534 <+132>:	pop	{r11, pc}
   0x00010538 <+136>:			; <UNDEFINED> instruction: 0x000105bc
   0x0001053c <+140>:	cmnvs	r2, r4, ror #6
   0x00010540 <+144>:	ldrdeq	r0, [r1], -r8
   0x00010544 <+148>:	andeq	r0, r1, r0, lsl r6
End of assembler dump.

```

初步分析和调试下代码

![](/media/15122339822130.jpg)


上图红框中最关键的几行代码，只要满足 r3 r2 相等，就可以完成此题。调试发现 r2 每次都是0x61626364，字符串就是 `dcba`（小端）。

r2是相对pc的偏移，一般就是代码中的常量了。r3是相对r11（也就是fp）偏移-8。现在重点到看看r11。

r11是Frame Pointer地址（栈底），sp是栈顶，一般函数内的变量可以通过fp取相对偏移获取。程序的输入参数也是这样。

从上面我们输入超长数据的结果可知，超长数据覆盖了 `[r11,#-8]`，那程序大概就是简单的把输入存到字符数组中。

根据`sub sp,sp,#80`看到栈大小有80字节，也就是20个word。而r11是 sp+4后的值，这样我们可以看下整个Frame上的数据，在加上main第一行push也让sp减4，因此总共22个word。用命令 `x/22w $r11-84` 输出。

![](/media/15122365637942.jpg)


也就是把上图右下角的数值改为 0x61626364 就好了。
从第一个0x31313131算，需要17*4=64个字符，最后四个需要是`dcba`。

这样试试

![](/media/15122367482364.jpg)

![](/media/15122367796672.jpg)

## 通过

终于挑战通过。Yeah!

![](/media/15122368686347.jpg)

就像题目所说，是为了熟悉下 How the variables are laid out in memory。


# 题目 Stack2



todo


