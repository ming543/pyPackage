call plug#begin('~/.vim/plugged')
Plug 'davidhalter/jedi-vim'
Plug 'jiangmiao/auto-pairs'
Plug 'Yggdroot/indentLine'
Plug 'nvie/vim-flake8'
call plug#end()


"'设置编码'
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8
"'显示行号'
"set nu
"set number
set cursorline
set cul        
set cursorcolumn
set cuc        
set showmatch
"set paste
"set listchars=tab:>-,trail:-
"'让vimrc配置变更立即生效'
autocmd BufWritePost $MYVIMRC source $MYVIMRC
" 打开文件类型检测 "
filetype on
" 打开语法高亮显示 "
syntax on

filetype plugin on
" 按 F5 執行當前 Python 程式碼"
map <F5> :call PRUN()<CR>
func! PRUN()
    exec "w" 
    if &filetype == 'python'
        exec "!python3 %"
    endif
endfunc
