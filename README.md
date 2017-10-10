# brute_force_attack_on_triple_des_with_reduced_key_space

mysterytwisterc3 的一道题
brute_force_attack_on_triple_des_with_reduced_key_space

题目
key的前几个字符是在2006年发明用于攻击DES密文的暴力破解机器
这个机器攻击 DES key (56 Bit) 仅仅花费不到一周
这个机器的名字就是key的前几位
后面还加上了6位数字
然后将这个字符串Hex后, 作为3DES加密使用的Key.
搜索找到这个机器的名字:
COPACOBANA

做题时遇到的一些坑和问题：
1、题目说是 机器名+6位数字 Hex后当做Key，但是Hex后字符串长度变为32，不能作为3DES的密钥，而后发现是直接将原来的字符串作为密钥，，
（至少作为解密函数的Key参数输入时是没有Hex的）
2、给的密文是16进制的，还需要将其decode后再传入解密函数，，
3、筛选解出的明文时有些问题，开始想到的遍历密文字母看其是否合法非常耗时，而且不奏效，有大佬用的是正则匹配，我这里知道密文后就偷懒
一下，包含‘COPACOBANA’的就是明文了。
4、发现好多个6位数字都可以解出正确的明文，，，
   008880--119991之间的以 80、81、90、91结尾的数字都可以


--str.zfill（）会返回指定长度字符串，右对齐，前面补0