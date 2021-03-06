#! python3

# pw.py : paspard管理プログラム（脆弱性あり ）

import sys
import pyperclip

PASSWORD = {
		'e-mail' : 'aaaAAA',
		'blog' : 'bbbBBB',
		'web' : 'cccCCC' }

if len(sys.argv) < 2:
	print('''[ pw.py の使い方 ]
第二引数にアカウントを入力すると、クリップボードに
パスワードがコピーされます''')
	exit()

account = sys.argv[1]

if account in PASSWORD:
	pyperclip.copy(PASSWORD[account])
	print('{}のパスワードをコピーしました'.format(account))
else:
	print('{}のアカウントはありませんでした'.format(account))


