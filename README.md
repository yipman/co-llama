# Co-Llama

Co-Llama is a personal AI assistant and user companion that speaks with the tone, style, and personality of characters from popular Sci-Fi media. This project is a Python-based implementation of a conversational AI assistant that can be used to chat with users and respond to their queries.


![image](https://github.com/yipman/co-llama/assets/547379/256d89f4-3fcf-425f-aaac-2961fb05c6d3)

## Features

✅ Conversational AI assistant that responds to user input

✅ Supports multiple modes: Performance (Online - Groq/Llama3-8B), Privacy (Offline - Local/Llama3-8B), Quality (Online - Groq/Llama3-70B)

✅ Supports multiple roles: Samantha (Her), C3PO (Star Wars), etc.

✅ Can play audio responses using Amazon Polly

❌ Can display responses in Markdown format

✅ Can be run as a standalone application or as a system tray icon on Windows

✅ Supports Light / Dark mode

## Getting Started

To use Co-Llama, simply run the `co-llama.py` file and interact with the application using the GUI. The application also has as a system tray icon on Windows where the user can show/hide Co-Llama.

## ToolGenerator Class

The ToolGenerator class is responsible for generating Python tools based on user input. The class has a single method generate_tool that takes a user_input parameter, which is used to generate the tool.

### generate_tool Method

The generate_tool method generates a Python tool based on the user input. The method consists of the following steps:

Prompt Generation: The method generates a prompt that asks the user to write a Python function that takes an input of type [input_type] and returns an output of type [output_type]. The prompt also includes the tool pipeline code.

Tool Generation: The method sends the prompt to the user and receives the generated tool code.

Refinement: The method refines the generated tool code to optimize its performance and accuracy.

Documentation: The method generates a document that describes the refined tool, including its name, description, input type, usage, pipeline, and output type.

Code Generation: The method generates the Python code for the tool based on the refined tool code and saves it in a .py file.

Return Response: The method returns the response from the tool maker.

### Code Generation

The code generation process involves the following steps:

Parsing the documented_tool string: The method parses the documented_tool string to extract the tool name, description, input type, output type, pipeline, and usage.

Generating the tool code: The method generates the Python code for the tool based on the parsed values.

Saving the code: The method saves the generated code in a .py file.

### Return Response

The method returns the response from the tool maker, which includes the generated tool code and other relevant information.

### Class Variables

The ToolGenerator class has the following class variables:

tool_name: The name of the generated tool.

tool_description: The description of the generated tool.

input_type: The input type of the generated tool.

output_type: The output type of the generated tool.

pipeline: The pipeline code of the generated tool.

tool_usage: The usage of the generated tool.

### Method Variables

The generate_tool method has the following method variables:

user_input: The user input used to generate the tool.

tool: The generated tool code.

refined_tool: The refined tool code.

documented_tool: The documented tool string.

tool_name: The name of the generated tool.

tool_description: The description of the generated tool.

input_type: The input type of the generated tool.

output_type: The output type of the generated tool.

pipeline: The pipeline code of the generated tool.

tool_usage: The usage of the generated tool.

## Contributing

Contributions are welcome! If you'd like to contribute to Co-Llama, please fork the repository and submit a pull request with your changes. Please make sure to follow the coding conventions and style guidelines used in the project.

## License

Co-Llama is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Credits

Co-Llama was created by Alejandro Rean. Special thanks to the Meta team for their work on the LLaMA model, and to the AWS team for their work on Amazon Polly.

## Contact

If you have any questions or feedback, please don't hesitate to reach out to me at arean@synaxis.com.ar .
