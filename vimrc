
" vim-plug settings
call plug#begin('~/.vim/plugged')
" Make sure you use single quotes
Plug 'scrooloose/nerdtree'
nnoremap <F2> :NERDTree<CR>
nnoremap <F3> :NERDTreeClose<CR>
Plug 'kien/ctrlp.vim'
Plug 'godlygeek/tabular'
Plug 'powerline/powerline'
set guifont=PowerlineSymbols\ for\ Powerline
"set nocompatible
set t_Co=256
let g:Powerline_symbols = 'fancy'
Plug 'plasticboy/vim-markdown'
if has("tags")  
    set tags=tags  
endif  
set autochdir
let Tlist_WinHeight = 20
let Tlist_WinWidth = 20
let Tlist_Compact_Format = 1
let Tlist_Max_Submenu_Items = 100 " default=25
let Tlist_Max_Tag_Length = 100 " default=10
let Tlist_Use_Horiz_Window = 1

Plug 'itchyny/calendar.vim'
let g:calendar_first_day = "monday"
let g:date_endian = "big"
let g:date_separator = "-"
let g:calendar_week_number = 1
let g:calendar_task = 1
let g:calendar_views = ['year', 'month', 'week', 'day_4', 'day', 'clock']
let g:calendar_yank_deleting = 1 " default
let g:calendar_cache_directory = '~/.cache/calendar.vim/' " default
nmap <F8>  :Calendar<CR>

call plug#end()            " required


" Vim Color Schema —— Molokai
"set t_Co=256
set background=dark
color molokai


" Quickly Run Code
map <F4> :call CompileRun()<CR>

func! CompileRun()
    exec "w"
    if &filetype == 'c'
        exec '!gcc % -o %<'
        exec '!time ./%<'
    elseif &filetype == 'cpp'
        exec '!g++ % -o %<'
        exec '!time ./%<'
    elseif &filetype == 'python'
        "exec '!time pythonw %'
        exec '!time pythonw -W ignore %'
    elseif &filetype == 'lua'
        exec '!time lua %'
    elseif &filetype == 'sh'
        :!time bash %
    elseif &filetype == 'dot'
        exec '!dot % -Tpng -o %<.png && open %<.png'
    endif
endfunc

" 光标居中
"set scrolloff=999


" 折叠
set foldenable
set foldmethod=syntax
set foldcolumn=0
setlocal foldlevel=1
set foldlevelstart=99
nnoremap <space> @=((foldclosed(line('.')) < 0) ? 'zc' : 'zo')<CR>


" Basic Settings
set hls
syntax on
set nocompatible
"filetype plugin on
nmap <F1> :vertical botright help<CR>
set pastetoggle=<F12>         " 使用<F12>切换paste模式，相当于下面两句话：
                              " :set paste
                              " :set nopaste
set fileformats=unix,dos      " 打开文件时可以同时支持UNIX格式和MS-DOS格式

set ai                        " 自动缩进
set showmatch                 " 代码匹配
set laststatus=2              " 总是显示状态行
set expandtab                 " 以下三个配置配合使用，设置tab和缩进空格数
set shiftwidth=4
set tabstop=4
set cursorline                " 为光标所在行加下划线
set number                    " 显示行号
set autoread                  " 文件在Vim之外修改过，自动重新读入

set ignorecase                " 检索时忽略大小写
set fileencodings=utf-8,gbk   " 使用utf-8或gbk打开文件
set encoding=utf-8           " 在屏幕上用utf-8编码显示
set helplang=cn               " 将帮助系统设置为中文
set showcmd

"set nocompatible
"filetype plugin on
"syntax on

iab iidate <c-r>=strftime("%Y%m%d")<cr>
iab iitime <c-r>=strftime("%Y-%m-%d %H:%M:%S")<cr>
