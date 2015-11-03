require 'sinatra'


# In here, all slides need to be added to a new URL

get '/_template' do
  	erb :_template
end

get '/eu-gesetzesgebung' do
	erb :'wire/eu-gesetzesgebung/index'
end 
