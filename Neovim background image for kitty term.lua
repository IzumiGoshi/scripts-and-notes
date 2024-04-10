-- NOTE:  Show terminal (kitty) background image
--          since it's not supported by neovim.
--          Set termimal bg color to match the current them
--          then set neovim color to transparent so terminal bg is used.

-- TODO: save and reset the terminal bg color on closing.

-- get the bg colors. returns a string like '# Normal xxx guifg=#c0caf5 guibg=#1a1b26'
local op = vim.api.nvim_exec2(':hi Normal', { ['output'] = true })
local hi_vals = op['output']
local bg_val = '000000' -- default to pure black bg...

for s in string.gmatch(hi_vals, 'guibg=#(.+)') do
  bg_val = s
end

-- WARN: Trying to use sed causes a headache.
--       Trying to call it from lua's os.exec causes brain damage.
local sed_cmd = 'sed -i ' .. '"s/^background #.\\+/background #' .. bg_val .. '/g"' .. ' "/home/chris/.config/kitty/kitty.conf"'

os.execute(sed_cmd)
-- trigger kitty to reload it's config file.
os.execute 'kill -SIGUSR1 $KITTY_PID'
-- set the neovim background color to none so it's transparent.
vim.cmd 'hi Normal guibg=NONE'
