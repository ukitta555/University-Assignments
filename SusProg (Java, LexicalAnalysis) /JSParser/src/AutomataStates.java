enum AutomataState {
    IDENTIFIER_NAME_EXTRACTION,
    IDENTIFIER_IS_RESERVED,
    NUMBER_EXTRACTION,
    NUMBER_IS_HEX,
    NUMBER_IS_DECIMAL,
    NUMBER_IS_FLOAT,
    PUNCTUATION_EXTRACTION,
    OPERATOR_EXTRACTION,
    COMMENT_EXTRACTION,
    STRING_EXTRACTION,
    ERROR_STATE
}
