# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Currently supported versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of our project seriously. If you have discovered a security vulnerability, please report it to us privately.

### How to Report

**DO NOT** create a public GitHub issue for security vulnerabilities.

Instead, please email us directly at:
**jose.santiago.echevarria@outlook.com**

Include the following information:
- Type of vulnerability (e.g., SQL injection, XSS, authentication bypass)
- Full paths of source file(s) related to the vulnerability
- Location of the affected source code (tag/branch/commit or direct URL)
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the vulnerability

### Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Fix Timeline**: Depends on severity
  - **Critical**: 7-14 days
  - **High**: 14-30 days
  - **Medium**: 30-60 days
  - **Low**: 60-90 days

### Security Measures

This project implements the following security measures:

- Input validation and sanitization
- Secure password hashing (where applicable)
- Environment variable protection
- Dependency vulnerability scanning
- Regular security audits
- Code review process

### Disclosure Policy

- Vulnerability reports are acknowledged within 48 hours
- We investigate and validate the vulnerability
- We develop and test a fix
- We release the fix and credit the reporter (if desired)
- We publicly disclose the vulnerability details after fix deployment

### Bug Bounty Program

Currently, we do not have a bug bounty program. However, we greatly appreciate responsible disclosure and will publicly acknowledge researchers who report valid vulnerabilities.

## Security Best Practices for Users

1. **Keep Dependencies Updated**: Regularly update all dependencies
2. **Environment Variables**: Never commit `.env` files or expose secrets
3. **Access Control**: Implement proper authentication and authorization
4. **Input Validation**: Always validate and sanitize user input
5. **HTTPS**: Use HTTPS in production environments
6. **Regular Audits**: Run security scans regularly

## Contact

For security concerns: jose.santiago.echevarria@outlook.com

For general issues: [Open an issue](https://github.com/josemsantiago/stockapp/issues)
