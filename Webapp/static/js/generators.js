const pythonGenerator = new Blockly.Generator('Python');

pythonGenerator.ORDER_ATOMIC = 0;

pythonGenerator.forBlock['pixel_set'] = function(block) {
    const x = block.getFieldValue('X');
    const y = block.getFieldValue('Y');
    const on = block.getFieldValue('on');
    const code = `set_pixel(${x}, ${y}, '${on}')\n`;
    return code;
};

export default pythonGenerator;