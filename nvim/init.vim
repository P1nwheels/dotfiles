call plug#begin('~/.vim/plugged')

Plug 'morhetz/gruvbox'
Plug 'tpope/vim-commentary'
Plug 'dracula/vim', { 'as': 'dracula' }
Plug 'sheerun/vim-polyglot'
Plug 'chrisbra/colorizer'
Plug 'arcticicestudio/nord-vim'
" Plug 'Kjwon15/vim-transparent'
Plug 'rainglow/vim'
Plug 'kevinhwang91/rnvimr'

call plug#end()

" Just normal things to use :)

set termguicolors

colorscheme codecourse
" set background=dark

syntax on
set nocompatible
set guicursor=
set noerrorbells
set hidden
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set number
set relativenumber
set smartcase
set noswapfile
set nobackup
set incsearch
set scrolloff=10

" All my remaps baby

inoremap kj <ESC>
nnoremap <C-h> :ColorHighlight<CR>
nnoremap<C-,> :ColorClear<CR>

" For rnvimr
let g:rnvimr_ex_enable = 1

nmap <space>r :RnvimrToggle<CR>
