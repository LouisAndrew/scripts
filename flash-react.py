#!/usr/bin/python3

# boilerplate snippets.
index_snippet = '''
import {$1} from './$2';

export default $1;'''

initial_file_snippet = '''
import React from 'react'
// import styling libs
// import local components

type Props = {

}

const $1: React.FC<Props> = () => {

	return <></>
}

export {$1}
'''

test_file_snippet = '''
import React from 'react'
import ReactDOM from 'react-dom'
import renderer from 'react-test-renderer'

// import { render, cleanup } from '@testing-library/react'
import { cleanup } from '@testing-library/react'
import '@testing-library/jest-dom'

import $1  from '$2'

describe('$1', () => {
    const Element = <$1 />

    afterEach(cleanup)

    it('renders without crashing', () => {
		const div = document.createElement('div')
		ReactDOM.render(Element, div)
	})
	
	/* it('renders correctly', () => {
		const { getByTestId } = render()
	}) */

	it('matches snapshot', () => {
		const run = false
	    
        if (run) {
	        const tree = renderer.create(Element).toJSON()
	        expect(tree).toMatchSnapshot()
	    }
	})
})
'''

# format string from component-name to ComponentName
def format_string (component_name):
    names = component_name.split('-')
    formatted_names = []

    for word in names:
        formatted_names.append(word.capitalize())

    return ''.join(formatted_names)


import sys

# 1st arg: component's name!
# 2nd arg: path from src.
# 3rd arg: options
[ arg, component_name, path, *options ] = sys.argv
with_options = len(sys.argv) > 3

import os

root_dir = os.getcwd()

path_with_src = root_dir + '/src/' + path + '/' + component_name

# first create directory for the component.
os.makedirs(path_with_src, exist_ok=True)
os.chdir(path_with_src)

# create basic components!
index_file = open('index.ts', 'w+')
initial_file = open(component_name + '.tsx', 'w+')

formatted_component_name = format_string(component_name)

# write snippets to its file.
index_file.write(index_snippet.replace('$1', formatted_component_name).replace('$2', component_name))
initial_file.write(initial_file_snippet.replace('$1', formatted_component_name))

# create test directory..
os.chdir(root_dir + '/src') # go back to project root dir.
test_file = open('__tests__/' + path + '/' + component_name + '.test.tsx', 'w+')

# write snippets into test directory.
test_file.write(test_file_snippet.replace('$1', formatted_component_name).replace('$2', path + '/' + component_name))
