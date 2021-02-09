call plug#begin('~/.vim/plugged')

Plug 'morhetz/gruvbox'
Plug 'tpope/vim-commentary'
Plug 'dracula/vim', { 'as': 'dracula' }
Plug 'sheerun/vim-polyglot'
Plug 'chrisbra/colorizer'
Plug 'arcticicestudio/nord-vim'
Plug 'Kjwon15/vim-transparent'

call plug#end()

" Just normal things to use :)

set termguicolors

colorscheme nord
" set background=dark

syntax on
set nocompatible
set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set number
" set relativenumber
set smartcase
set noswapfile
set nobackup
set incsearch

" All my remaps baby

inoremap kj <ESC>
nnoremap <C-h> :ColorHighlight<CR>

