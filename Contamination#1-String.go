package kata
import "strings"

func Contamination(text, char string) string {
  return strings.Repeat(char, len(text))
}
